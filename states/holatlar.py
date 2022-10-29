from aiogram.dispatcher.filters.state import State,StatesGroup

class  Murojaat(StatesGroup):
    ism_holati = State()
    fam_holati = State()
    tel_holati = State()
    yosh_holati = State()
    maqsad_holati = State()
    tasdiqlash_holati = State()