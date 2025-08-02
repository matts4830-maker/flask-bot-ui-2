def check_target():
    import time
    with open("target_pokemon_bot.log", "a") as log:
        log.write("Checking Target at " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
    time.sleep(2)
