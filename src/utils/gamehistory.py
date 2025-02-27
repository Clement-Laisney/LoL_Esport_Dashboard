from utils import RiotAPI
from datetime import timedelta, datetime

api = RiotAPI()


def get_player_game_data(puuid: str, participants_data: list) -> dict:
    for participant in participants_data:
        if participant.get("puuid") == puuid:
            return participant


def get_game_history_info(matchIds: list, puuid: str) -> list[dict]:
    history_data_list = []
    for matchid in matchIds:
        data = api.get_match_by_match_id(matchId=matchid).get("info")

        duration = data.get("gameDuration")
        timestamp = data.get("gameEndTimestamp")
        queueId = data.get("queueId")

        playerGameData = get_player_game_data(
            puuid=puuid, participants_data=data.get("participants")
        )

        championName = playerGameData.get("championName")
        isWin = playerGameData.get("win")

        history_data_list.append(
            {
                "isWin": isWin,
                "duration": duration,
                "timestamp": timestamp,
                "queueId": queueId,
                "championName": championName,
            }
        )
    return history_data_list


def convert_duration_to_min_sec(duration: int) -> tuple[str]:
    days, minutes, seconds = str(timedelta(seconds=duration)).split(":")
    return minutes, seconds


def convert_timestamp_to_occurence_str(timestamp: int) -> str:
    now = datetime.now()
    enddate = datetime.fromtimestamp(timestamp=(timestamp / 1e3))
    date = now - enddate
    if date < timedelta(minutes=1):
        sec = str(int(date)).split(":")[-1]
        occurence = f"{sec} second{'s' if int(sec)>1 else ''} ago"
    elif date < timedelta(hours=1):
        minutes = str(date).split(":")[1]
        occurence = f"{minutes} minute{'s' if int(minutes)>1 else ''} ago"
    elif date < timedelta(days=1):
        hours = str(date).split(":")[0]
        occurence = f"{hours} hour{'s' if int(hours)>1 else ''} ago"
    else:
        days = date.days
        occurence = f"{days} day{'s' if int(days)>1 else ''} ago"
    return occurence


def convert_queueid_to_gamemode(queueId: int) -> str:
    print(queueId)
    if queueId == 0:
        gamemode = "Custom"
    elif queueId == 400:
        gamemode = "Draft"
    elif queueId == 420:
        gamemode = "Ranked Solo/Duo"
    elif queueId == 440:
        gamemode = "Ranked Flex"
    elif queueId == 450:
        gamemode = "ARAM"
    elif queueId == 490:
        gamemode = "Normal"
    elif queueId == 700 or queueId == 720:
        gamemode = "Clash"
    elif queueId == 870 or queueId == 880 or queueId == 890:
        gamemode = "Co_op vs. AI"
    else:
        gamemode = "Unknown"
    return gamemode
