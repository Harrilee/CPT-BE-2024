# -*- coding: utf-8 -*-
import pickle
from django.http import JsonResponse

from core.models import WebUser
from core.services.parser import get_scenario_list
from core.services.gameModel import MiniGame, Text



def initializeGame(user: WebUser) -> MiniGame:

    scenario_list = get_scenario_list()
    patient_names = []
    scenario_list[0].start_sentence = "欢迎来到菜鸟咨询师小游戏！在这个游戏里，您将扮演一名心理咨询专业的大一学生，在导师的带领下，为十六位性少数男性来访者解决他们的困扰。让我们开始吧!"
    for i in range(len(scenario_list) - 1):
        scenario_list[i].set_next_node(scenario_list[i + 1])

    start_sentence = Text(MiniGame.start_sentence, 'supervisor', scenario_list[0])

    for scenario in scenario_list:
        patient_names.append(scenario.name)


    game = MiniGame(start_sentence,user,patient_names)
    return game





def getNewGame(phoneNumber: str) -> MiniGame|JsonResponse:
    try:
        webUser = WebUser.objects.get(phone_number=phoneNumber)
    except WebUser.DoesNotExist:
        print("User does not exist")
        return JsonResponse({'error': '用户不存在'})

    # print('currentDay', webUser.currentDay)
    # check if game is initialized in web user
    if webUser.game is None:
        print("Game not initialized")
        game = initializeGame(webUser)
        # use pickle serialization for game
        pickle_game = pickle.dumps(game)
        webUser.game = pickle_game
        webUser.save()
        return game
    else:
        print("Game already initialized")
        game = pickle.loads(webUser.game)
        game.user = webUser
        return game

