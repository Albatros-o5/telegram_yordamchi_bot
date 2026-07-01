from aiogram import Router, F
from aiogram.filters import Command
from keyboards.reply import reply_keyboard
from keyboards.inline import support_keyboard
from aiogram.types import Message
from database.repository import MarketRepository


class MarketBot:
    def __init__(self, db: MarketRepository):
        self.db = db
        self.router = Router()
        self._register_handlers()

    def _register_handlers(self):
        self.router.message(Command("start"))(self.start)
        self.router.message(Command("reg"))(self.reg)
        self.router.message(Command("list"))(self.list)
        self.router.message(Command("del"))(self.delete)
        self.router.message(Command("res"))(self.restart)
        self.router.message(Command("help"))(self.help)
        self.router.message(Command("support"))(self.support)
        self.router.message(Command("update"))(self.update)
        self.router.message(Command("get_db"))(self.get_db)
        self.router.message(F.text == "🖥️ List")(self.list)
        self.router.message(F.text == "🛒 Total")(self.total)
        self.router.message(F.text == "🚑 Help")(self.help)
        self.router.message(F.text == "🗑️ Reset")(self.restart)
        self.router.message(F.photo)(self.texts)
        self.router.message(F.video)(self.texts)
        self.router.message(F.sticker)(self.texts)
        self.router.message(F.voice)(self.texts)
        self.router.message(F.document)(self.texts)
        self.router.message(F.text)(self.texts)

    async def start(self, message: Message):
        await message.answer(f"{message.from_user.first_name}, Market Botga xush kelibsiz!\n\nBot qanday ishlashini bilish uchun /help buyrug'ini yuboring.", reply_markup=reply_keyboard)

    async def reg(self, message: Message):
        parts = message.text.strip().split()

        if len(parts) != 3:
            await message.answer("Iltimos, to'g'ri formatda ma'lumot kiriting: /reg <mahsulot> <narx>")
            return

        product = parts[1]
        try:
            cost = float(parts[2].replace(",", "."))
        except ValueError:
            await message.answer("Iltimos, narxni to'g'ri formatda kiriting.")
            return
        user_id = message.from_user.id
        self.db.add_db(user_id, product, cost)
        await message.answer(f"Ma'lumot qo'shildi: {product} - {cost} so'm")

    async def list(self, message: Message):
        user_id = message.from_user.id

        info = self.db.show_market(user_id)

        if not info:
            await message.answer("🕸️Ro'yxat bo'sh.")
            return

        text = "🐳Ro'yxat\n\n"
        total = 0

        for item in info:
            total += item.cost
            text += f"🔹 <b>{item.product}</b>\n   💰 {item.cost:,.0f} so'm   (ID: {item.id})\n\n"
        text += "━━━━━━━━━━━━━━━\n"
        await message.answer(text, parse_mode="HTML")

    async def delete(self, message: Message):
        part = message.text.strip().split()

        if len(part) != 2 or not part[1].isdigit():
            await message.answer("To'g'ri formatda kiriting.")
            return

        user_id = message.from_user.id

        self.db.dell_market(int(part[1]), user_id)
        await message.answer("Ma'lumot o'chirildi")

    async def restart(self, message: Message):

        user_id = message.from_user.id

        self.db.drop_market(user_id)

        await message.answer("🕸️Ro'yxat tozalandi")

    async def help(self, message: Message):
        await message.answer(
            "📌 <b>Xarajatlar Hisoblagichi Boti</b>\n\n"
            "Bu bot kunlik xarajatlaringizni yozib borish va jami sarf-xarajatlaringizni hisoblashga yordam beradi.\n\n"

            "📝 <b>Buyruqlar:</b>\n\n"

            "➕ <b>/reg mahsulot narx</b>\n"
            "Yangi xarajat qo'shish.\n"
            "Misol: <code>/reg Non 5000</code>\n\n"

            "📋 <b>/list</b>\n"
            "Barcha xarajatlaringizni ko'rsatadi.\n\n"

            "💰 <b>Total</b>\n"
            "Jami xarajatlaringizni hisoblaydi.\n\n"

            "❌ <b>/del ID</b>\n"
            "Kerakli xarajatni ID bo'yicha o'chiradi.\n"
            "Misol: <code>/del 3</code>\n\n"

            "♻️ <b>/update mahsulot narx ID</b>\n"
            "Ma'lumotni yangilash imkonini beradi.\n"
            "Misol: <code>/update olma 25000 1</code>\n\n"

            "🗑️ <b>/res</b>\n"
            "Barcha xarajatlar ro'yxatini tozalaydi.\n\n"

            "🆘 <b>/support</b>\n"
            "Bot bo'yicha yordam yoki takliflar uchun bog'lanish.\n\n"

            "💡 Xarajat qo'shgandan so'ng <b>/list</b> yoki <b>Total</b> orqali xarajatlaringizni kuzatib boring.",
            parse_mode="HTML"
        )

    async def total(self, message: Message):
        user_id = message.from_user.id

        info = self.db.show_market(user_id)

        if not info:
            await message.answer("Kechirasiz ma'lumot topilmadi.\n\nMa'lumot borligiga ishonch hosil qiling /list.")
            return

        total = 0
        for item in info:
            total += item.cost

        text = (
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💰 <b>Jami Xarajat</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            f"💵 <b>{total:,.0f} so'm</b>"
        )

        await message.answer(text,  parse_mode="HTML")

    async def support(self, message: Message):
        await message.answer("Murojaat uchun bu yerga yozsangiz bo'ladi",
                             reply_markup=support_keyboard)

    async def update(self, message: Message):

        parts = message.text.strip().split()

        if len(parts) != 4 or not parts[2].isdigit():
            await message.answer("Ma'lumotni to'g'ri formatda kirgizing😶‍🌫️")
            return

        product = parts[1]
        user_id = message.from_user.id
        cost = float(parts[2].replace(",", "."))
        id = int(parts[3])

        items = self.db.get_market(id, user_id)

        if not items:
            await message.answer("Bunaqa tartibli mahsulot yo'q.")
            return

        self.db.update_market(id, user_id, product, cost)

        await message.answer("Ma'lumot yangilandi.")

    async def texts(self, message: Message):
        await message.answer("To'g'ri buyruq kirgizing.\n\n/help")

    async def get_db(self, message: Message):
        parts = message.text.strip().split()
        if len(parts) != 3:
            await message.answer("Format: /get_db <id> <user_id>")
            return
        id = int(parts[1])
        user_id = message.from_user.id
        item = self.db.get_market(id, user_id)
        if not item:
            await message.answer("Mahsulot topilmadi.")
            return
        await message.answer(f"🔹 {item.product} — {item.cost:,.0f} so'm (ID: {item.id})")


db = MarketRepository()
handlers = MarketBot(db)
router = handlers.router
