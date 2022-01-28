duration = 4153

if duration < 60: # 1 минута = 60 секунд
    print (duration, 'сек')
elif 3600 > duration >= 60:  # 1 минута = 60 секунд
    minutes = duration//60
    seconds = duration%60
    print(minutes, 'мин', seconds, 'сек')
elif 86400> duration >= 3600:  # 1 час = 3600 секунд, 1 день = 86400 секунд
    hours = duration//3600
    minutes = (duration-(hours*3600))%60
    seconds= duration%60
    print(hours, 'часов', minutes, 'минуты', seconds, 'секунды')
elif  duration >= 86400:  # 1 день =604800 секунд
    days = duration//86400
    hours = (duration%86400)//3600
    minutes = (duration%3600)//60
    seconds = duration%60
    print (days, 'дней', hours, 'часов', minutes, 'минут', seconds, 'секунд')
