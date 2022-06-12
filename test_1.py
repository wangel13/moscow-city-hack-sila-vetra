import re
from simhash import Simhash, SimhashIndex
def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

data = {
    1: '''Москва заняла первое место среди европейских городов в рейтинге
инноваций, помогающих в борьбе с COVID-19
В мире Москва занимает третье место, уступая лишь Нью-Йорку и Сан-Франциско.
Москва признана первой среди европейских городов в рейтинге инноваций,
помогающих в формировании устойчивости коронавирусу. Она опередила Лондон и
Барселону.
Среди мировых мегаполисов российская столица занимает третью строчку —
после Сан-Франциско и Нью-Йорка. Пятерку замыкают Бостон и Лондон. Рейтинг
составило международное исследовательское агентство StartupBlink.
Добиться высоких показателей Москве помогло почти 160 передовых решений,
которые применяются для борьбы с распространением коронавируса.
Среди них алгоритмы компьютерного зрения на основе искусственного
интеллекта. Это методика уже помогла рентгенологам проанализировать более трех
миллионов исследований.
Еще одно инновационное решение — облачная платформа, которая объединяет
пациентов,
врачей,
медицинские
организации,
страховые
компании,
фармакологические производства и сайты.
Способствовали высоким результатам и технологии, которые помогают
адаптировать жизнь горожан во время пандемии. Это проекты в сфере умного туризма,
электронной коммерции и логистики, а также дистанционной работы и
онлайн-образования.
Эксперты агентства StartupBlink оценивали принятые в Москве меры с точки
зрения эпидемиологических показателей и влияния на экономику.
''',
    2: '''Москва стала лидером в Европе в рейтинге инноваций, помогающих в борьбе
с COVID-19
В мире российская столица заняла третье место, обогнав Лондон и Барселону.
Москва заняла первое место среди европейских городов в рейтинге инноваций,
помогающих в борьбе с COVID-19, опередив Лондон и Барселону. Об этом сообщает
портал мэра и правительства Москвы. В мире российская столица заняла третье место,
уступив лишь Нью-Йорку и Сан-Франциско.
В российской столице применяются почти 160 передовых решений для борьбы с
распространением коронавируса. Среди них алгоритмы компьютерного зрения на
основе искусственного интеллекта, а такжеоблачная платформа, которая объединяет
пациентов,
врачей,
медицинские
организации,
страховые
компании,
фармакологические производства и сайты. Способствовали высоким результатам и
технологии, которые помогают горожанам адаптироваться во время пандемии. Это
проекты в сфере умного туризма, электронной коммерции и логистики, а также
дистанционной работы и онлайн-образования.
Рейтинг составляется на базе глобальной карты инновационных решений по
борьбе с коронавирусом и оценивает около 100 ведущих городов и 40 стран мира.''',
    3: '''Москва заняла первое место в Европе по инновациям в борьбе с COVID-19
Москва обошла европейские столицы в рейтинге инноваций по устойчивости к
COVID-19, опередив Лондон и Барселону, сообщается на официальном сайте мэра
Москвы.
Российская столица также заняла третье место среди мировых мегаполисов. В
пятерку лидеров вошли Бостон и Лондон.
Занять лидирующие позиции в рейтинге Москве помогли около 50 передовых
решений, которые применяются для борьбы с распространением COVID-19.
Одно из таких решений - алгоритмы компьютерного зрения на основе
искусственного интеллекта, которые уже помогли рентгенологам проанализировать
более трех миллионов исследований.
Также
высоким
результатам
способствовали
технологии,
помогающие
адаптировать жизнь москвичей во время пандемии. Среди них - проекты в сфере
умного туризма, электронной коммерции и логистики, дистанционной работы и
онлайн-образования.
Эксперты
оценивали,
как
принятые
в
Москве
меры
влияют
на
эпидемиологические показатели и экономику.''',
    4: '''Москва заняла первое место в Европе по инновациям в борьбе с COVID-19
Исследовательское агентство StartupBlink составило рейтинг городов по
инновациям, помогающим в борьбе с COVID-19. Москва заняла в нем третье место в
мире и первое — среди европейских городов.
«Среди мировых мегаполисов российская столица занимает третью строчку —
после Сан-Франциско и Нью-Йорка. Пятерку замыкают Бостон и Лондон»,— говорится
на сайте московской мэрии.
Среди московских инноваций, используемых для борьбы с коронавирусом,—
алгоритмы
компьютерного
зрения
на
основе
искусственного
интеллекта
(задействованы в медицинских исследованиях), облачная платформа (объединяет
пациентов,
врачей,
медицинские
организации,
страховые
компании,
фармакологические производства и сайты), технологии для адаптации к жизни в
городе в период пандемии (проекты в сфере «умного» туризма, электронной
коммерции и логистики, а также дистанционной работы и онлайн-образования).
По словам мэра Москвы Сергея Собянина, по состоянию на конец ноября
большинство отраслей экономики столицы «чувствуют себя нормально». По данным
мэрии, в 2021 году в Москве около 25 тыс. предприятий малого и среднего бизнеса
получили поддержку властей.''',
5: '''Москва стала первой в Европе среди городов с инновациями по борьбе с
COVID-19
Москва заняла первое место среди европейских городов в рейтинге инноваций,
которые помогают бороться с коронавирусом. Об этом сообщает пресс-служба мэрии
столицы.
Рейтинг составило международное исследовательское агентство «StartupBlink».
Среди европейских столиц Москва стала первой, обогнав Лондон и Барселону, а среди
мировых городов – третьей, уступив Нью-Йорку и Сан-Франциско.
Как отметили в мэрии Москвы, добиться таких высоких показателей помогли
почти 160 передовых инноваций, среди которых алгоритмы компьютерного зрения на
основе искусственного интеллекта, облачная платформа, объединившая пациентов,
врачей, медицинские организации, страховые компании, фармакологические
производства и сайты, а также технологии, которые помогают адаптировать жизнь
горожан во время пандемии – проекты в сфере «умного» туризма, электронной
коммерции и логистики, дистанционной работы и онлайн-образования.
При этом в правительстве города подчеркнули, что при введении антиковидных
ограничений власти отказались от крайностей, сделав ставку на профилактику
заболевания – увеличили количество пунктов с бесплатным тестированием и
вакцинацией, запатентовали онлайн-программы и платформы для обучения, и
занялись развитием телемедицины.''',
6: '''Москва заняла восьмое место среди европейских городов в рейтинге
инноваций, помогающих в борьбе с COVID-19
В мире Москва занимает лишь восьмое место, уступая в том числе Нью-Йорку и
Сан-Франциско.
Москва лишь пятой среди европейских городов в рейтинге инноваций,
помогающих в формировании устойчивости коронавирусу. Она пропустила вперёд как
Лондон, так и Барселону. Рейтинг составило международное исследовательское
агентство StartupBlink.
Добиться высоких показателей Москве помогло почти 70 передовых решений,
которые применяются для борьбы с распространением коронавируса.
Среди них алгоритмы компьютерного зрения на основе искусственного
интеллекта. Это методика уже помогла рентгенологам проанализировать более
пятисот тысяч исследований.
Еще одно инновационное решение — облачная платформа, которая объединяет
пациентов,
врачей,
медицинские
организации,
страховые
компании,
фармакологические производства и сайты.
Способствовали высоким результатам и технологии, которые помогают
адаптировать жизнь горожан во время пандемии. Это проекты в сфере умного туризма,
электронной коммерции и логистики, а также дистанционной работы и
онлайн-образования.
Эксперты агентства StartupBlink оценивали принятые в Москве меры с точки
зрения эпидемиологических показателей и влияния на экономику.''',
7: '''Бостон занял первое место среди европейских городов в рейтинге инноваций
в медицине, а Андроново отказалось от участия в оценке
Бостон признан первым среди европейских городов в рейтинге инноваций,
помогающих в формировании устойчивости коронавирусу. Он опередил Лондон,
Барселону и Андроново.
В мире Бостон занимает третье место, уступая лишь Нью-Йорку и Сан-Франциско.
Андроново не участвовало в оценке в этом году. Рейтинг составило международное
исследовательское агентство StartupBlink.
Обойти преследователей Бостону помогло более 100 передовых решений,
которые применяются для борьбы с распространением коронавируса.
В свою очередь Андроново уже несколько лет не участвует в рейтинге по причине
отсутствия кислорода в атмосфере города и водорода в составе воды в реке Лене.
В качестве инновационного решения, позволяющего исправить положение,
неким человеком на улице было предложено использовать фаршированных
гонобобелем голубей для обеспечения регулярного авиасообщения с планетой
Железяка.
Другое предложенное решение оказалось ещё более странным, чем предыдущее
— облачная платформа, которая объединяет перистые и кучевые облака в
сверхмассивный кластер инновационных перисто-кучевых облаков.
Такого рода высокие технологии вряд ли помогут Андронову занять какое-либо
место в каком-нибудь конкурсе.''',
8: '''Проектный офис ФЭСН РАНХиГС завершает 30 проектов. И начинает новые.
Ежегодно в мае-июне Проектный офис Факультета экономических и социальных
наук завершает работу над бизнес-проектами и представляет результаты заказчикам –
российским и международным компаниям.
Среди компаний-заказчиков были крупные российские компании и организации:
Сбер, РЖД, ВЭБ, Минстрой РФ, Ростуризм, Правительство Москвы, киностудия им.
Горького, холдинг САВООВ ФУДС, Альфа-Банк, ВТБ, Дом РФ, Очаково, Сегежа-Групп а
также представительства зарубежных компаний: BMW, DeLonghi, L’Oreal, Pfizer, Ritter
Sport, Xiaomi, Avon, Schneider Group и др.
Проектный офис ФЭСН является крупнейшим университетским проектным
центром не только по количеству и сложности проектов, и не только по количеству
студентов-участников. Он уже создал и создает новые масштабные форматы проектной
работы. Так, еще пять лет назад ФЭСН вовлек в проектную деятельность университеты
пяти стран Европы и стал разрабатывать с ними полугодичные проекты для
международных компаний на английском языке. Некоторые сложные проекты
делались усилиями проектных групп нескольких стран; например, в проекте от
генерального директора BMW Russia по «Разработке маркетинговой стратегии
перехода компании BMW с бензиновых двигателей на электрические в России»
бакалавры ФЭСН работали вместе с магистрами из Германии и Бельгии. А в одном из
проектов участвовали команды из Германии, Бельгии, Италии, 4 проектные группы из
Франции и 5 из Бразилии.''',
}

for k in data:
    data[k] = data[k].replace('\r', '').replace('\n', '')

objs = [(str(k), Simhash(get_features(v))) for k, v in data.items()]
index = SimhashIndex(objs, k=12)

print(index.bucket_size())

origin = '''Москва заняла первое место среди европейских городов в рейтинге инноваций, помогающих в борьбе с COVID-19 В мире Москва занимает третье место, уступая лишь Нью-Йорку и Сан-Франциско.
Москва признана первой среди европейских городов в рейтинге инноваций, помогающих в формировании устойчивости коронавирусу. Она опередила Лондон и Барселону.

Среди мировых мегаполисов российская столица занимает третью строчку — после Сан-Франциско и Нью-Йорка. Пятерку замыкают Бостон и Лондон. Рейтинг составило международное исследовательское агентство StartupBlink.

Добиться высоких показателей Москве помогло почти 160 передовых решений, которые применяются для борьбы с распространением коронавируса.

Среди них алгоритмы компьютерного зрения на основе искусственного интеллекта. Это методика уже помогла рентгенологам проанализировать более трех миллионов исследований.

Еще одно инновационное решение — облачная платформа, которая объединяет пациентов, врачей, медицинские организации, страховые компании, фармакологические производства и сайты.

Способствовали высоким результатам и технологии, которые помогают адаптировать жизнь горожан во время пандемии. Это проекты в сфере умного туризма, электронной коммерции и логистики, а также дистанционной работы и онлайн-образования.

Эксперты агентства StartupBlink оценивали принятые в Москве меры с точки зрения эпидемиологических показателей и влияния на экономику.

Московский опыт
В борьбе с коронавирусом Москва отказалась от крайностей. Ставку сделали на профилактику: увеличили количество пунктов бесплатного экспресс-тестирования и вакцинации, запатентовали онлайн-программы и платформы для обучения, развивали возможности телемедицины.

Московская система здравоохранения за время пандемии накопила достаточно большой запас прочности, который позволяет не останавливать плановую и экстренную помощь даже в периоды пиков заболеваемости COVID-19.

Столица поддерживает бизнес, выделяя субсидии и предоставляя льготы. В этом году мерами поддержки воспользовалось около 25 тысяч предприятий малого и среднего бизнеса.

Как составляется рейтинг
Рейтинг составляется на базе глобальной карты инновационных решений по борьбе с коронавирусом и оценивает около 100 ведущих городов и 40 стран мира. Глобальная карта была создана в марте 2020 года, и в течение года на нее было добавлено более тысячи решений.

Алгоритм рейтинга учитывает количество и тип инноваций, которые используются в борьбе с коронавирусом. Проекты, которые принимались к рассмотрению, должны были отвечать трем базовым критериям, среди которых инновационность, релевантность (решение должно непосредственно отвечать на вызовы COVID-19) и достоверность. Дополнительные баллы присуждаются за отдельные выдающиеся инициативы. Все решения проходят предварительную модерацию и отбираются экспертами по критериям качества и достоверности информации.'''


origin2 = '''
На пресс-конференции в «Роскосмосе» Дмитрий Рогозин раскрыл параметры полёта военного спутника «Космос-2555». По его словам, спутник переведён в режим управления «На кого Бог пошлёт».

Космос-2555 был запущен с космодрома Плесецк 29 апреля. На орбиту его вывела ракета лёгкого класса «Ангара-1.2». Назначение спутника официально не раскрывалось, однако из разговоров сотрудников «Роскосмоса» в соцсетях стало известно, что это спутник оптической разведки. Судя по литере «Z», нанесённой на его борт, он должен был выполнять задачи в ходе спецоперации на Донбассе. Наблюдая за траекторией спутника, западные разведки поспешили заявить, что он потерял управление и неконтролируемо снижается, однако глава «Роскосмоса» заверил, что именно так и планировалось.

«То, что Космос-2555 не управляется, это заведомая ложь. Но управляется он не нами, а самим Господом. Режим «На кого Бог пошлёт» - это эксклюзивный, доступный лишь русским способ наведения спутников, когда само Провидение решает, на чью голову обрушить нашу карающую длань массой 3,5 тонны», - рассказал Рогозин.

Глава «Роскосмоса» добавил, что день и ночь молится о том, чтобы Всевышний избрал целью для спутника головы тех, кто ввёл незаконные и необоснованные санкции против российской космической отрасли. Из-за этого Россия не получает импортных электронных компонентов, и Космос-2555 стал последним российским разведывательным спутником.

Пока готовился этот материал, стало известно, что спутник с литерой «Z» сгорел в атмосфере, не достигнув вражеских целей.
'''

origin = origin.replace('\r', '').replace('\n', '')

s1 = Simhash(get_features(origin))
print(index.get_near_dups(s1))

index.add(9, s1)
print(index.get_near_dups(s1))

for k, v in data.items():
    print(Simhash(v).distance(s1))

print(s1.distance(s1))