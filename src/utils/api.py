import os
from dotenv import load_dotenv
import requests

load_dotenv()


class RiotAPI:
    def __init__(self, api_token=os.environ["RIOT_API_KEY"]) -> None:
        self.__api_token = api_token
        self.__headers = {"X-Riot-Token": api_token}

    def __str__(self) -> str:
        return "RiotAPI"

    def __repr__(self) -> str:
        return f"<RiotAPI>"

    def get_account_by_riot_id(self, gameName: str, tagLine: str) -> dict:
        """Retrieve the encrypted 78 character puuid with game name end tagline.

        Args:
            gameName (str): Game name string
            tagLine (str): A 3 character string

        Returns:
            dict: return a dictionnary with puuid, gameName and tagLine
        """
        r = requests.get(
            url=f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}",
            headers=self.__headers,
        )
        return r.json()

    def get_summoner_by_puuid(self, puuid: str) -> dict:
        """Retrieve the summmoner ids by the puuid.

        Args:
            puuid (str): The 78 character long puuid string

        Returns:
            dict: return a dictionnary with :
                    accountId (str): Encrypted account ID. Max length 56 characters.
                    profileIconId (int): ID of the summoner icon associated with the summoner.
                    revisionDate (float): Date summoner was last modified specified as epoch milliseconds. The following events will update this timestamp: summoner name change, summoner level change, or profile icon change.
                    id (str): Encrypted summoner ID. Max length 63 characters.
                    puuid (str): Encrypted PUUID. Exact length of 78 characters.
                    summonerLevel (float): Summoner level associated with the summoner.
        """
        r = requests.get(
            url=f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}",
            headers=self.__headers,
        )
        return r.json()

    def get_league_by_summoner_id(self, summonerId: str) -> list[dict]:
        """Retrieve league entries in all queues for a given summoner

        Args:
            summonerId (str): Player's encrypted summonerId.

        Returns:
            list[dict]: A list of dictionnary with:
                        leagueId (str): A unique id of the league
                        summonerId (str): Player's encrypted summonerId.
                        queueType (str): The name of the Queue (RANKED_SOLO_5x5, RANKED_FLEX_SR, ...)
                        tier (str): The name of the tier (IRON, BRONZE, SILVER ...)
                        rank (str): The player's division within a tier. (I,II,III)
                        leaguePoints (int): The number of LP.
                        wins (int): Winning team on Summoners Rift.
                        losses (int): Losing team on Summoners Rift.
                        hotStreak (bool)
                        veteran (bool)
                        freshBlood (bool)
                        inactive (bool)
        """
        r = requests.get(
            url=f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summonerId}",
            headers=self.__headers,
        )
        return r.json()

    def get_match_ids_by_puuid(
        self,
        puuid: str,
        startTime: float = None,
        endTime: float = None,
        queue: int = None,
        matchType: str = None,
        start: int = 0,
        count: int = 20,
    ) -> list[str]:
        """Retrieve the list of match ids by puuid

        Args:
            puuid (str): The 78 character long puuid string
            startTime (float, optional): Epoch timestamp in seconds. The matchlist started storing timestamps on June 16th, 2021. Any matches played before June 16th, 2021 won't be included in the results if the startTime filter is set. Defaults to None.
            endTime (float, optional): Epoch timestamp in seconds. Defaults to None.
            queue (int, optional): Filter the list of match ids by a specific queue id. This filter is mutually inclusive of the type filter meaning any match ids returned must match both the queue and type filters. Defaults to None.
            matchType (str, optional): Filter the list of match ids by the type of match. This filter is mutually inclusive of the queue filter meaning any match ids returned must match both the queue and type filters. Defaults to None, possibilities: ranked, normal, tourney, tutorial.
            start (int, optional): Start index. Defaults to 0.
            count (int, optional): Valid values: 0 to 100. Number of match ids to return. Defaults to 20.

        Returns:
            list[str]: Return a list of match ids
        """
        payload = {
            "startTime": startTime,
            "endTime": endTime,
            "queue": queue,
            "type": matchType,
            "start": start,
            "count": count,
        }

        r = requests.get(
            url=f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids",
            headers=self.__headers,
            params=payload,
        )
        return r.json()

    def get_match_by_match_id(self, matchId: str) -> dict:
        """Retrieve mmatch entriesy match id

        Args:
            matchId (str): The match id string

        Returns:
            dict: Return a json. To understand structure visit: https://developer.riotgames.com/apis#match-v5/GET_getMatch
        """
        r = requests.get(
            url=f"https://europe.api.riotgames.com/lol/match/v5/matches/{matchId}",
            headers=self.__headers,
        )
        return r.json()

    def get_match_timeline_by_match_id(self, matchId: str) -> dict:
        """Retrieve the timeline of the match

        Args:
            matchId (str): The match id string

        Returns:
            dict: Return a json. To understand structure visit: https://developer.riotgames.com/apis#match-v5/GET_getTimeline
        """
        r = requests.get(
            url=f"https://europe.api.riotgames.com/lol/match/v5/matches/{matchId}/timeline"
        )
        return r.json()


api = RiotAPI()


def retrieve_player_data(gamename: str, tagline: str) -> dict:
    player_data = api.get_account_by_riot_id(gameName=gamename, tagLine=tagline)

    summoner_data = api.get_summoner_by_puuid(puuid=player_data.get("puuid"))

    league_data = api.get_league_by_summoner_id(summonerId=summoner_data.get("id"))

    data = {**player_data, **summoner_data, "league": league_data}

    return data
