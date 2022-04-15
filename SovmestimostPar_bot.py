import logging
import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.executor import start_webhook

TOKEN = ('5325195406:AAEGEoaPwFlzpfoYMZdGw4oH1Ka_EcHFxsQ')
bot = Bot(TOKEN)
dp = Dispatcher(bot)
HEROKU_APP_NAME = os.getenv('sovmestimostparbot')

WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}' 

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)

async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()

@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, '👋Привет, я бот проверки на совместимость по ЗЗ👋 \n\n✍️Напиши свой Знак Зодиака и Знак Зодиака партнёра с которым хочешь проверить совеместимость✍️\n \n🚨Обязательно что бы знак женщины был слева, иначе совместимость может быть расчитана не правильно🚨 \n \nПРИМЕР:\nводолей + овен. ПРОБЕЛ между + и знаками зодиака ОБЯЗАТЕЛЕН')
    
@dp.message_handler()
async def oven(message : types.Message):

    if message.text.lower() == 'овен + овен':
        await bot.send_message(message.from_user.id, '<b>♈Совместимы на 91%♈</b>\n\nОни одинаковые, но есть одно но: каждый из них настолько ярко проявляет свои гендерные роли, что они кажутся совершенно разными.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'овен + телец':
        await bot.send_message(message.from_user.id, '<b>♈Совместимы на 81%♉</b>\n\n Она сможет оставаться яркой и активной рядом с ним, он – медлительным, но настойчивым. И когда ее внешний напор встречается с его внутренним, начинается молчаливая схватка двух упрямцев. Потом они влюбляются друг в друга и бороться становится еще интереснее.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'овен + близнецы':
        await bot.send_message(message.from_user.id, '<b>♈Совместимы на 72%♊</b>\n\nОна огненная, он воздушный. Он может дать ей разгореться еще сильнее или наоборот, затушить ее пламя. Она его, конечно, не обожжет, но точно останется надолго в его памяти.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'овен + рак':
        await bot.send_message(message.from_user.id, '<b>♈Совместимы на 81%♋</b>\n\nОна – яркая и строптивая, он – нерешительный и сентиментальный. Кажется, они друг для друга именно то, что нужно. Конечно, ссор не избежать – но мириться они будут так сладко, что полюбят эти ссоры.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'овен + лев':
        await bot.send_message(message.from_user.id, '<b>♈Совместимы на 97%♌</b>\n\nОба они приналежат к стихии Огня: яркие и энергичные, вспыхивают быстро и так же быстро сгорают.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'овен + дева':
        await bot.send_message(message.from_user.id, '<b>♈Совместимы на 84%♍</b>\n\nЕсли она — это пожар, то он — портативный огнетушитель. Удобный, практичный, своевременный.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'овен + весы':
        await bot.send_message(message.from_user.id, '<b>♈Совместимы на 83%♎</b>\n\nВозможно, это нестандартное распределение ролей — настойчивая женщина и податливый мужчина — но им самим такое положение вещей очень даже нравится.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'овен + скорпион':
        await bot.send_message(message.from_user.id, '<b>♈Совместимы на 76%♏</b>\n\nЖенщина-Овен принадлежит к разряду тех женщин, кто не привык долго ждать и берет инициативу в свои руки, а мужчина-Скорпион из тех, кто любит, когда женщина проявляет себя четко и самостоятельно.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'овен + стрелец':
        await bot.send_message(message.from_user.id, '<b>♈Совместимы на 92%♐</b>\n\nВ ней, конечно, больше огня, но и он не промах. Но сможет ли эта яркая собственница примириться с исключительным свободолюбием мужчины-Стрельца?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'овен + козерог':
        await bot.send_message(message.from_user.id, '<b>♈Совместимы на 82%♑</b>\n\nЖенщина-Овен поражает своим напором, мужчина-Козерог — своей упорностью. Такие похожие слова, и такой разный смысл.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'овен + водолей':
        await bot.send_message(message.from_user.id, '<b>♈Совместимы на 82%♒</b>\n\nОна — яркая и напористая, он — непредсказуемый и свободолюбивый. Сумеет ли она удержать его? Сумеет ли он оказать ей достойное сопротивление, но не переборщить?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'овен + рыбы':
        await bot.send_message(message.from_user.id, '<b>♈Совместимы на 87%♓</b>\n\nОни очень разные. Она — яркость и напор, он — мягкость и бездействие. Возможно, она сумеет зарядить его.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'телец + овен':
        await bot.send_message(message.from_user.id, '<b>♉Совместимы на 72%♈</b>\n\nОна — мягкая, но упрямая, он — строптивый, порывистый, страстный. Он вполне может показать ей, какая энергия прячется внутри нее самой. Но нужно ли ей это?', parse_mode=types.ParseMode.HTML)    
    elif message.text.lower() == 'телец + телец':
        await bot.send_message(message.from_user.id, '<b>♉Совместимы на 87%♉</b>\n\nОни стоят друг друга. Наконец-то у каждого их них нашелся достойный друг. Или соперник?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'телец + близнецы':
        await bot.send_message(message.from_user.id, '<b>♉Совместимы на 73%♊</b>\n\nОна – приземленная и очень практичная, он – легкий и ветренный. Сумеет ли он надолго задержаться рядом с ней?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'телец + рак':
        await bot.send_message(message.from_user.id, '<b>♉Совместимы на 83%♋</b>\n\nЖенщина-Телец и мужчина-Рак совершенно точно сумеют создать прочные и долгие отношения, ведь у них так много точек соприкосновения.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'телец + лев':
        await bot.send_message(message.from_user.id, '<b>♉Совместимы на 88%♌</b>\n\nИх отношения — это союз земной невозмутимости и огненной страсти. Хотя, постойте — до союза там далеко.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'телец + дева':
        await bot.send_message(message.from_user.id, '<b>♉Совместимы на 92%♍</b>\n\nОни так похожи. Оба настроены на длительные и честные отношения. Не будет ли им скучно друг с другом?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'телец + весы':
        await bot.send_message(message.from_user.id, '<b>♉Совместимы на 92%♎</b>\n\nОна — земная и практичная, он — возвышенный идеалист. Сумеет ли она «спустить его на землю» или он заставит ее сбросить груз земных забот?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'телец + скорпион':
        await bot.send_message(message.from_user.id, '<b>♉Совместимы на 98%♏</b>\n\nОни представляют собой противоположности. Она не любит громких слов и яркой страсти, он же, напротив, живет только этим. Смогут ли эти двое найти что-то общее?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'телец + стрелец':
        await bot.send_message(message.from_user.id, '<b>♉Совместимы на 81%♐</b>\n\nОна — приземленная, спокойная и рассудительная. Он — оптимистичный, неугомонный. Что они смогут друг другу дать?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'телец + козерог':
        await bot.send_message(message.from_user.id, '<b>♉Совместимы на 89%♑</b>\n\nОни подходят друг другу почти так же, как женщина-Козерог и мужчина-Телец.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'телец + водолей':
        await bot.send_message(message.from_user.id, '<b>♉Совместимы на 83%♒</b>\n\nОна — земная, стабильная, любит комфорт и удовольствия. Он — неземной, нестабильный, и на комфорт ему плевать.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'телец + рыбы':
        await bot.send_message(message.from_user.id, '<b>♉Совместимы на 91%♓</b>\n\nОни неплохо подходят друг другу. Она — приземленная и заботливая, он — отстраненный и чувствительный.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'близнецы + овен':
        await bot.send_message(message.from_user.id, '<b>♊Совместимы на 83%♈</b>\n\nОни составят интересную пару: она — непостоянная и ускользающая, он — страстный и импульсивный. Сумеет ли он ее удержать?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'близнецы + телец':
        await bot.send_message(message.from_user.id, '<b>♊Совместимы на 73%♉</b>\n\nОна — легкая и непостоянная, он — сама стабильность и постоянство. Смогут ли они вместе достичь гармонии?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'близнецы + близнецы':
        await bot.send_message(message.from_user.id, '<b>♊Совместимы на 84%♊</b>\n\nОба они — воздушны, легкие, любящие общение и развлечения. Кажется, они сумеют найти общий язык.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'близнецы + рак':
        await bot.send_message(message.from_user.id, '<b>♊Совместимы на 67%♋</b>\n\nЖенщина-Близнецы – воздушная, переменчивая. Мужчина-Рак – застенчивый, внутренне противоречивый. Она сможет раскрепостить его, а он обеспечит ей нежность и покой.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'близнецы + лев':
        await bot.send_message(message.from_user.id, '<b>♊Совместимы на 81%♌</b>\n\nОна — живая и непосредственная, он — яркий и очень честолюбивый. Сможет ли она увлечься им?',parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'близнецы + дева':
        await bot.send_message(message.from_user.id, '<b>♊Совместимы на 93%♍</b>\n\nЖенщина-Близнецы отличается воздушностью, а мужчина-Дева — наоборот, практичностью и приземленностью. Найдут ли они о чем поговорить?',parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'близнецы + весы':
        await bot.send_message(message.from_user.id, '<b>♊Совместимы на 89%♎</b>\n\nОни оба — воздушные, любят общение и друг друга. Особенно друг друга.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'близнецы + скорпион':
        await bot.send_message(message.from_user.id, '<b>♊Совместимы на 93%♏</b>\n\nИх различие в том, что она пытается не драматизировать ни при каких обстоятельствах, а он — гуру драматизации.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'близнецы + стрелец':
        await bot.send_message(message.from_user.id, '<b>♊Совместимы на 98%♐</b>\n\nЭто две противоположности. Которые, как известно, притягиваются. Со страшной силой.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'близнецы + козерог':
        await bot.send_message(message.from_user.id, '<b>♊Совместимы на 82%♑</b>\n\nОна – легка, несколько поверхностная, он – строгий, даже суровый. Кажется, сложно придумать более разных персонажей. Но они встретились и даже захотели быть вместе. Почему?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'близнецы + водолей':
        await bot.send_message(message.from_user.id, '<b>♊Совместимы на 93%♒</b>\n\nОни очень похожи. Оба принадлежат к стихии Воздуха, отсюда и глубинное взаимопонимание.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'близнецы + рыбы':
        await bot.send_message(message.from_user.id, '<b>♊Совместимы на 82%♓</b>\n\nЖенщина-Близнецы и мужчина-Рыбы вполне могут составить счастье друг друга.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рак + овен':
        await bot.send_message(message.from_user.id, '<b>♋Совместимы на 91%♈</b>\n\nОна — нежная, неуловимая, смешливая, скромная и сексуальная одновременно. Он — сильный, смелый, активный — огненный! Теперь понимаете, почему они мечтают друг о друге?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рак + телец':
        await bot.send_message(message.from_user.id, '<b>♋Совместимы на 93%♉</b>\n\nКажется, они созданы друг для друга: она — нежная и такая семейная, он — чрезвычайно заботливый и спокойный.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рак + близнецы':
        await bot.send_message(message.from_user.id, '<b>♋Совместимы на 77%♊</b>\n\nОна — нежная и осторожная, он — весельчак и повеса. Он точно ее очарует.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рак + рак':
        await bot.send_message(message.from_user.id, '<b>♋Совместимы на 83%♋</b>\n\nКогда они встречаются, им кажется, что они нашли друг друга. Возможно, это действительно так.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рак + лев':
        await bot.send_message(message.from_user.id, '<b>♋Совместимы на 82%♌</b>\n\nЭто люди разных стихий, разного склада. Она — мягкая, нежная, пленительная. Он — царственный и важный. Похоже на Татьяну и Онегина — остается надеяться, что их отношения все же не обречены.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рак + дева':
        await bot.send_message(message.from_user.id, '<b>♋Совместимы на 84%♍</b>\n\nОна — идеальная жена, он — лучший муж, по мнению многих. Слишком идеально, не так ли?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рак + весы':
        await bot.send_message(message.from_user.id, '<b>♋Совместимы на 94%♎</b>\n\nОни оба любят любовь, но немного по-разному.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рак + скорпион':
        await bot.send_message(message.from_user.id, '<b>♋Совместимы на 91%♏</b>\n\nОна – сама нежность, он – чистая страсть. Где та золотая середина, на которой они наконец встретятся и захотят поделиться друг с другом тем, что из себя представляют?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рак + стрелец':
        await bot.send_message(message.from_user.id, '<b>♋Совместимы на 82%♐</b>\n\nРак и Стрелец — знаки трудносовместимые: там, где Рак хочет осесть и остепениться, у Стрельца только начинается веселая кочевая жизнь.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рак + козерог':
        await bot.send_message(message.from_user.id, '<b>♋Совместимы на 96%♑</b>\n\nОни полные противоположности. Любят друг друга, но бегут друг от друга.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рак + водолей':
        await bot.send_message(message.from_user.id, '<b>♋Совместимы на 84%♒</b>\n\nОна мягкая и нежная, он порывистый, «воздушный». Найдут ли они точки соприкосновения?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рак + рыбы':
        await bot.send_message(message.from_user.id, '<b>♋Совместимы на 90%♓</b>\n\nОни оба принадлежат к Водной стихии, так что понимают, чего хотят — они сами и те, кого они любят.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'лев + овен':
        await bot.send_message(message.from_user.id, '<b>♌Совместимы на 99%♈</b>\n\nОни оба знают, чего хотят. Поэтому долго не раздумывают, быть им вместе или нет.', parse_mode=types.ParseMode.HTML)    
    elif message.text.lower() == 'лев + телец':
        await bot.send_message(message.from_user.id, '<b>♌Совместимы на 91%♉</b>\n\nНа расстоянии они нравятся друг другу больше, чем вблизи.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'лев + близнецы':
        await bot.send_message(message.from_user.id, '<b>♌Совместимы на 68%♊</b>\n\nЭта пара может похвастаться тем, что вместе они найдут выход из любой ситуации: благодаря неиссякаемому энтузиазму женщины-Льва и обширным связям мужчины-Близнеца.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'лев + рак':
        await bot.send_message(message.from_user.id, '<b>♌Совместимы на 71%♋</b>\n\nЭто союз воды и огня: будет чувственно и горячо.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'лев + лев':
        await bot.send_message(message.from_user.id, '<b>♌Совместимы на 87%♌</b>\n\nЭто встреча двух царей — точнее, царя и царицы. Скорее всего, они так и не сумеют определить, кто из них победил в соревновании на величественность, но кое-что они все же для себя выяснят.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'лев + дева':
        await bot.send_message(message.from_user.id, '<b>♌Совместимы на 86%♍</b>\n\nОна — страстная, он — холодный. Вероятно, их притягивает друг к другу именно в силу такой противоположности характеров.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'лев + весы':
        await bot.send_message(message.from_user.id, '<b>♌Совместимы на 79%♎</b>\n\nОни достаточно разные, чтобы привлечь внимание друг друга — и достаточно похожие, чтобы продолжить знакомство.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'лев + скорпион':
        await bot.send_message(message.from_user.id, '<b>♌Совместимы на 98%♏</b>\n\nОни оба — огненные, порывистые, сложные. Им будет страшно интересно вместе.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'лев + стрелец':
        await bot.send_message(message.from_user.id, '<b>♌Совместимы на 90%♐</b>\n\nОни очень похожи. Яркие, самодостаточные — особенно она.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'лев + козерог':
        await bot.send_message(message.from_user.id, '<b>♌Совместимы на 76%♑</b>\n\nОна такая жаркая, а он такой холодный. Они точно полюбят друг друга.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'лев + водолей':
        await bot.send_message(message.from_user.id, '<b>♌Совместимы на 97%♒</b>\n\nОна – полная эгоистка, он же – законченный альтруист. Как думаете, кто в этой паре будет центром Вселенной?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'лев + рыбы':
        await bot.send_message(message.from_user.id, '<b>♌Совместимы на 83%♓</b>\n\nОна — яркая и страстная, он — нежный и робкий. Они должны неплохо друг другу подойти.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'дева + овен':
        await bot.send_message(message.from_user.id, '<b>♍Совместимы на 71%♈</b>\n\nОна — земная, он — огненный. Когда они соединяются, они могут свернуть горы.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'дева + телец':
        await bot.send_message(message.from_user.id, '<b>♍Совместимы на 69%♉</b>\n\nОни оба земные, практичные. Им будет комфортно друг с другом. Но интересно ли?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'дева + близнецы':
        await bot.send_message(message.from_user.id, '<b>♍Совместимы на 75%♊</b>\n\nОни оба находятся под управлением Меркурия. Ее планета наделяет здоровой практичностью и скептицизмом, его – высокой контактностью и легкостью характера. Смогут ли они чем-то поделиться друг с другом?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'дева + рак':
        await bot.send_message(message.from_user.id, '<b>♍Совместимы на 81%♋</b>\n\nОна — практичная, он — ранимый. Думается, они отлично подойдут друг другу.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'дева + лев':
        await bot.send_message(message.from_user.id, '<b>♍Совместимы на 73%♌</b>\n\nЕй может быть непонятна его страсть к славе и влиянию. Он же не разделит ее скромности.')
    elif message.text.lower() == 'дева + дева':
        await bot.send_message(message.from_user.id, '<b>♍Совместимы на 75%♍</b>\n\nОни так похожи, что просто не могут не заметить друг друга. Но смогут ли они по-настоящему заинтересоваться друг другом – вот это вопрос.', parse_mode=types.ParseMode.HTML) 
    elif message.text.lower() == 'дева + весы':
        await bot.send_message(message.from_user.id, '<b>♍Совместимы на 74%♎</b>\n\nОна любит порядок, он — гармонию. Посмотрим, насколько совместимы эти понятия.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'дева + скорпион':
        await bot.send_message(message.from_user.id, '<b>♍Совместимы на 98%♏</b>\n\nОна – практична и порядочна. Он – горяч и хладнокровен одновременно. Их встреча похожа на встречу удава и мышки – очень хитрой мышки.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'дева + стрелец':
        await bot.send_message(message.from_user.id, '<b>♍Совместимы на 72%♐</b>\n\nОна совсем не любит спешить, он же мчится на всех парусах, чтобы успеть. Совпадут ли когда-нибудь их ритмы?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'дева + козерог':
        await bot.send_message(message.from_user.id, '<b>♍Совместимы на 61%♑</b>\n\nОни оба – воплощение практичности и стабильности. Не станет ли им скучно друг с другом?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'дева + водолей':
        await bot.send_message(message.from_user.id, '<b>♍Совместимы на 72%♒</b>\n\nОна — та, которая твердо стоит на ногах, он – вечно витает в облаках. Удастся ли ей спустить его на землю?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'дева + рыбы':
        await bot.send_message(message.from_user.id, '<b>♍Совместимы на 67%♓</b>\n\nОна – сама рациональность и практичность. Он всегда расслаблен и имеет богатое воображение. Она привыкла к четкому графику, ему же по душе спонтанность и отсутствие рамок. Найдут ли они точки соприкосновения?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'весы + овен':
        await bot.send_message(message.from_user.id, '<b>♎Совместимы на 82%♈</b>\n\nОна – сама мягкость и дипломатичность, он же состоит из желания и нетерпения. Кажется, они созданы друг для друга. Или…', parse_mode=types.ParseMode.HTML)    
    elif message.text.lower() == 'весы + телец':
        await bot.send_message(message.from_user.id, '<b>♎Совместимы на 93%♉</b>\n\nОни так похожи: оба стремятся к гармонии и любви.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'весы + близнецы':
        await bot.send_message(message.from_user.id, '<b>♎Совместимы на 93%♊</b>\n\nЭто союз двух легких, воздушных людей. Иногда, впрочем, им будет просто необходимо приземлиться.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'весы + рак':
        await bot.send_message(message.from_user.id, '<b>♎Совместимы на 78%♋</b>\n\nОтношения между женщиной-Весы и мужчиной-Раком будут нежными и романтичными. Но крепкими ли?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'весы + лев':
        await bot.send_message(message.from_user.id, '<b>♎Совместимы на 89%♌</b>\n\nЕй нравится его огонь, ему — ее воздушность.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'весы + дева':
        await bot.send_message(message.from_user.id, '<b>♎Совместимы на 85%♍</b>\n\nОна — мягкая и романтичная, он — практичный, устойчивый, серьезный.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'весы + весы':
        await bot.send_message(message.from_user.id, '<b>♎Совместимы на 91%♎</b>\n\nПожалуй, это самый дипломатичный союз из всех возможных.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'весы + скорпион':
        await bot.send_message(message.from_user.id, '<b>♎Совместимы на 64%♏</b>\n\nОна специалист по внешней гармонии, он — по внутренней дисгармонии. Кажется, им нужно многое обсудить.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'весы + стрелец':
        await bot.send_message(message.from_user.id, '<b>♎Совместимы на 88%♐</b>\n\nОна – романтичная, он – оптимистичный. Она сглаживает острые углы, он попросту не обращает на них внимания.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'весы + козерог':
        await bot.send_message(message.from_user.id, '<b>♎Совместимы на 92%♑</b>\n\nОна — легкая и приятная, он — настоящий мужчина. Кажется, они нашли друг друга.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'весы + водолей':
        await bot.send_message(message.from_user.id, '<b>♎овместимы на 96%♒</b>\n\nОни оба не любят долгих выяснений отношений, а любят когда все легко, просто и хорошо.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'весы + рыбы':
        await bot.send_message(message.from_user.id, '<b>♎Совместимы на 81%♓</b>\n\nЖенщина-Весы и мужчина-Рыбы вместе составят красивую пару, она — нежная и бесконфликтная, он — тонкий и понимающий.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'скорпион + овен':
        await bot.send_message(message.from_user.id, 'Совместимы на 72%. Они оба страстные и знают, чего хотят. Главное, чтобы они хотели одного и того же.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'скорпион + телец':
        await bot.send_message(message.from_user.id, 'Совместимы на 60%. Она сама страсть, а он – покой. Она мятеж, он – безмятежность. Они действительно нуждаются друг в друге, но понимают это далеко не сразу.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'скорпион + близнецы':
        await bot.send_message(message.from_user.id, 'Совместимы на 58%. Они довольно разные. Он вряд ли разделит ее тягу к эмоционально насыщенной жизни.', parse_mode=types.ParseMode.HTML)    
    elif message.text.lower() == 'скорпион + рак':
        await bot.send_message(message.from_user.id, 'Совместимы на 89%. Они будут понимать друг друга с полуслова, потому что оба тонкие, чувственные, нежные и страстные. Они по-настоящему любят любовь.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'скорпион + лев':
        await bot.send_message(message.from_user.id, 'Совместимы на 92%. Они оба яркие и страстные — не много ли огня на двоих?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'скорпион + дева':
        await bot.send_message(message.from_user.id, 'Совместимы на 76%. Она — самая страстная представительница зодиака, он — самый прагматичный. Что между ними общего?')
    elif message.text.lower() == 'скорпион + весы':
        await bot.send_message(message.from_user.id, 'Совместимы на 77%. Женщина-Скорпион – пожалуй, самая страстная из всех, кто встречался на его пути. Он – робкий, застенчивый, дипломатичный. Сумеет ли она его раскрепостить и раскрыть так, чтобы ей самой стало невыносимо интересно?..', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'скорпион + скорпион':
        await bot.send_message(message.from_user.id, 'Совместимы на 94%. Это два сгустка кипучей энергии, страсти, завышенных амбиций и глубокой чувствительности. Оказавшись рядом, они вряд ли смогут отказаться от искушения попробовать друг друга на вкус.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'скорпион + стрелец':
        await bot.send_message(message.from_user.id, 'Совместимы на 92%. Она — любительница глубоких и интенсивных эмоций, он же предпочитает свободу и легкость. Сумеет ли она завладеть его сердцем?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'скорпион + козерог':
        await bot.send_message(message.from_user.id, 'Совместимы на 100%. Женщина-Скорпион — самая страстная из всех зодиакальных дам. Мужчина-Козерог — самый закрытый и строгий мужчина, которых вы когда либо встречали. Сумеет ли она раскрыть его? Под силу ли ему удержать ее?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'скорпион + водолей':
        await bot.send_message(message.from_user.id, 'Совместимы на 88%. Женщина-Скорпион и мужчина-Водолей сумеют поладить друг с другом. Оба они целеустремленные, бесшабашны и ценят внутреннюю свободу личности.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'скорпион + рыбы':
        await bot.send_message(message.from_user.id, 'Совместимы на 97%. Они оба — чувственные, страстные и нежные. Романтики между этими двумя будет море.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'стрелец + овен':
        await bot.send_message(message,from_user.id, 'Совместимы на 84%. Они оба яркие, огненные — довольно неплохо подходят друг другу.', parse_mode=types.ParseMode.HTML)    
    elif message.text.lower() == 'стрелец + телец':
        await bot.send_message(message,from_user.id, 'Совместимы на 72%. Она довольно яркая и активная, он же не привык особенно напрягаться. Интересно, сумеет ли она хотя бы немного растормошить его?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'стрелец + близнецы':
        await bot.send_message(message,from_user.id, 'Совместимы на 100%. Это представители противоположных знаков зодиака, именно поэтому им так непривычно хорошо вместе.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'стрелец + рак':
        await bot.send_message(message,from_user.id, 'Совместимы на 71%. Она — неутомимая оптимистка, он — скромный обольститель. Интересно, как будут складываться их отношения?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'стрелец + лев':
        await bot.send_message(message,from_user.id, 'Совместимы на 100%. Они оба — чистый огонь. Помогут ли они друг другу разгореться еще сильней?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'стрелец + дева':
        await bot.send_message(message,from_user.id, 'Совместимы на 82%. Они очень разные. Она — яркая и целеустремленная, настоящий энтузиаст. Он — спокойный и деловитый. Что связывает их?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'стрелец + весы':
        await bot.send_message(message,from_user.id, 'Совместимы на 92%. Они довольно неплохо подходят другу. Им будет приятно и нескучно вместе.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'стрелец + скорпион':
        await bot.send_message(message,from_user.id, 'Совместимы на 100%. Они оба страстные, уверенные в себе. Возможно, она немного робеет перед ним, но только поначалу.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'стрелец + стрелец':
        await bot.send_message(message,from_user.id, 'Совместимы на 100%. Если вы когда-нибудь видели людей, которые отражают друг друга, словно в зеркале, вероятно, это были женщина и мужчина-Стрелец.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'стрелец + козерог':
        await bot.send_message(message,from_user.id, 'Совместимы на 79%. Она нуждается в непрерывном развитии и частой смене впечатлений, он – в стабильности и постоянстве. Что они делают вместе?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'стрелец + водолей':
        await bot.send_message(message,from_user.id, 'Совместимы на 100%. Они оба порывистые, свободные и энергичные. Их пара похожа на союз солнца и ветра — звучит очень привлекательно, правда?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'стрелец + рыбы':
        await bot.send_message(message,from_user.id, 'Совместимы на 71%. Часто они думают одинаково. Общее мировоззрение значит для них больше, чем страсть и влечение.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'козерог + овен':
        await bot.send_message(message.from_user.id, 'Совместимы на 82%. Они подходят друг другу. Правда, иногда она будет уставать от его напора.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'козерог + телец':
        await bot.send_message(message.from_user.id, 'Совместимы на 86%. Она — само совершенство. Он — образец спокойствия и стабильности. Нужен ли им кто-то еще?', parse_mode=types.ParseMode.HTML)    
    elif message.text.lower() == 'козерог + близнецы':
        await bot.send_message(message.from_user.id, 'Совместимы на 71%. Она серьезная, строгая, правильная. Он – разгильдяй. Герой, от которого все без ума. Все, кроме неприступной женщины-Козерога.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'козерог + рак':
        await bot.send_message(message.from_user.id, 'Совместимы на 82%. Они — прямые противоположности друг друга. Интересно, что их все-таки связывает?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'козерог + лев':
        await bot.send_message(message.from_user.id, 'Совместимы на 83%. Возможно, ее будут раздражать его царские замашки.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'козерог + дева':
        await bot.send_message(message.from_user.id, 'Совместимы на 85%. Она — целеустремленная и прагматичная, он — «весь в себе»: практичный, работящий, эмоционально-закрытый. Они так похожи — не будет ли им скучно?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'козерог + весы':
        await bot.send_message(message.from_user.id, 'Совместимы на 81%. Мужчина-Весы, безусловно, сумеет найти подход к женщине-Козерогу. Она, в свою очередь, одарит его своим вниманием, которое, к слову, перепадает немногим.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'козерог + скорпион':
        await bot.send_message(message.from_user.id, 'Совместимы на 100%. Женщина-Козерог – воплощение холодной страсти. Она само совершенство, но некому растопить ее лед. Постойте, а как же мужчина-Скорпион?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'козерог + стрелец':
        await bot.send_message(message.from_user.id, 'Совместимы на 93%. Они оба любят достигать своих целей, но они у них такие разные. Женщина-Козерог и мужчина-Стрелец, несомненно, привлекут друг друга, но надолго ли?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'козерог + козерог':
        await bot.send_message(message.from_user.id, 'Совместимы на 84%. Они стоят друг друга. Оба практичные, целеустремленные и… зацикленные на себе.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'козерог + водолей':
        await bot.send_message(message.from_user.id, 'Совместимы на 82%. Это очень интересная пара. Она пытается его ограничить, а он никак не ограничивается.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'козерог + рыбы':
        await bot.send_message(message.from_user.id, 'Совместимы на 67%. Она любит разговаривать начистоту, он привык уходить от прямых вопросов. Найдут ли они общий язык?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'водолей + овен':
        await bot.send_message(message.from_user.id, 'Совместимы на 100%. Она – независимая и свободолюбивая, он – яркий собственник. Пожалуй, она для него – как раз то, что нужно.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'водолей + телец':
        await bot.send_message(message.from_user.id, 'Совместимы на 82%. Это союз стабильности и оригинальности, надежности и бесшабашности.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'водолей + близнецы':
        await bot.send_message(message.from_user.id, 'Совместимы на 93%. Они оба любят легкость и свободу в отношениях. Кажется, это идеальная пара.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'водолей + рак':
        await bot.send_message(message.from_user.id, 'Совместимы на 66%. Она стремится к свободе, он — к безопасности. Кажется, их графики не пересекаются. Хотя, постойте…', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'водолей + лев':
        await bot.send_message(message.from_user.id, 'Совместимы на 92%. Они притягиваются, как и положено противоположностям. И, соответственно, отталкиваются.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'водолей + дева':
        await bot.send_message(message.from_user.id, 'Совместимы на 67%. Они довольно разные. Она любит свободу, а он – порядок.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'водолей + весы':
        await bot.send_message(message.from_user.id, 'Совместимы на 100%. Они оба принадлежат к стихии воздуха, она – немного более оригинальная и свободолюбивая, он же приверженец долгих и глубоких отношений.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'водолей + скорпион':
        await bot.send_message(message.from_user.id, 'Совместимы на 89%. Она нежная, он страстный. Возможно, это оно из лучших сочетаний.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'водолей + стрелец':
        await bot.send_message(message.from_user.id, 'Совместимы на 100%. Они очень похожи: оба свободолюбивые и жизнерадостные. Возможно, они нашли друг друга.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'водолей + козерог':
        await bot.send_message(message.from_user.id, 'Совместимы на 92%. Она-оригинальна и свободолюбивая, он – суров, серьезен, но все-таки довольно мил. Интересно, сможет ли он удержать ее?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'водолей + водолей':
        await bot.send_message(message.from_user.id, 'Совместимы на 77%. Женщина-Водолей — это ураган, мужчина-Водолей — тоже. Когда они вместе, это двойной ураган — штука захватывающая и опасная.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'водолей + рыбы':
        await bot.send_message(message.from_user.id, 'Совместимы на 100%. У них похожие взгляды. Кажется, они сумеют понять друг друга достаточно глубоко.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рыбы + овен':
        await bot.send_message(message.from_user.id, 'Совместимы на 85%. Она — мечтательная и романтичная, он — смелый и напористый. Отличное сочетание.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рыбы + телец':
        await bot.send_message(message.from_user.id, 'Совместимы на 82%. Они неплохо понимают друг друга, правда, иногда он ей может показаться немного грубым и бесчувственным. А она ему — скучной и неинтересной.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рыбы + близнецы':
        await bot.send_message(message.from_user.id, 'Совместимы на 81%. Они и похожи, и очень отличаются. Попробуем разобраться, чем именно.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рыбы + рак':
        await bot.send_message(message.from_user.id, 'Совместимы на 83%. Они очень похожи. Непонятно только, это плюс в их случае или минус.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рыбы + лев':
        await bot.send_message(message.from_user.id, 'Совместимы на 95%. Она – нежная и неуловимая, он – харизматичный, знает о себе многое, в основном то, что он лучший. Сумеет ли он «поймать» ее?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рыбы + дева':
        await bot.send_message(message.from_user.id, 'Совместимы на 100%. Она погружена в себя, он практичен и реалистичен. Есть ли у них что-то общее?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рыбы + весы':
        await bot.send_message(message.from_user.id, 'Совместимы на 100%. Они оба нерешительные и стремящиеся к гармонии.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рыбы + скорпион':
        await bot.send_message(message.from_user.id, 'Совместимы на 100%. Они оба достаточно чувственны и эмоцинальны, чтобы прекрасно понимать друг друга. Где та грань, за которой их отличия начнут проявляться настолько ярко, чтобы они наконец заметили их?..', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рыбы + стреле':
        await bot.send_message(message.from_user.id, 'Совместимы на 74%. Женщина-Рыбы, пожалуй, самая неуловимая из всех. Мужчина-Стрелец тоже неуловим, но по-своему. Кто кого будет догонять?', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рыбы + козерог':
        await bot.send_message(message.from_user.id, 'Совместимы на 93%. Женщина-Рыбы и мужчина-Козерог — тот редкий случай, когда все сходится. Ну, или почти все.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рыбы + водолей':
        await bot.send_message(message.from_user.id, 'Совместимы на 93%. Они похожи: он не признает границ, а для нее любые границы уже давно стерты.', parse_mode=types.ParseMode.HTML)
    elif message.text.lower() == 'рыбы + рыбы':
        await bot.send_message(message.from_user.id, 'Совместимы на 100%. Это союз двух неуловимых и загадочных личностей, одна из которых к тому же и женщина.', parse_mode=types.ParseMode.HTML)
    else:
        await bot.send_message(message.from_user.id, 'Я вас не понимаю. Возможно вы написали без пробелов между знаками зодиака и + должен быть пробел', parse_mode=types.ParseMode.HTML)
    
    
    
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
