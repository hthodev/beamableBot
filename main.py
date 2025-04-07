import os
import time
import json
import random
import cloudscraper
from datetime import datetime
from colorama import Fore, Style, init
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor, as_completed
import re

# Initialize colorama
init(autoreset=True)

# Helper Function: Logger
def logger(message, level="info"):
    now = datetime.now().isoformat()
    colors = {
        "info": Fore.BLUE,
        "warn": Fore.YELLOW,
        "error": Fore.RED,
        "success": Fore.GREEN,
        "debug": Fore.MAGENTA,
    }
    color = colors.get(level, Fore.WHITE)
    print(f"{color}[{now}] [{level.upper()}]: {message}{Style.RESET_ALL}")

headers = {
    "accept": "text/x-component",
    "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "cache-control": "no-cache",
    "content-type": "text/plain;charset=UTF-8",
    "next-router-state-tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22modules%22%2C%7B%22children%22%3A%5B%5B%22moduleIdOrPath%22%2C%22questsold%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%5B%22moduleNestedId1%22%2C%227129%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%5D%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
    "origin": "https://hub.beamable.network",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://hub.beamable.network/modules/questsold/7129",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
}

def read_files():
    with open("proxies.txt", "r") as f:
        proxies = [line.strip() for line in f.readlines() if line.strip()]
    
    with open("cookies.txt", "r") as f:
        cookies = [line.strip() for line in f.readlines() if line.strip()]
    
    return proxies, cookies

def create_scraper(proxy=None):
    scraper = cloudscraper.create_scraper()
    if proxy:
        scraper.proxies = {
            "http": proxy,
            "https": proxy
        }
    return scraper

async def click_quest(cookie, session):
    async def quest_7129():
        try:
            url = 'https://hub.beamable.network/modules/questsold/7129'
            current_headers = headers.copy()
            current_headers["next-action"] = "eef77ac1785cc4d8ca64fb769a7cc5e0bc594592"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":7129,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":false,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like and Comment - GDC Schedule","progress":1,"affirmType":{"questId":7129,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":7129,"link":"https://x.com/BeamableNetwork/status/1901989668947960223"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},1614,"questsold",true,false]"""
            
            response = session.post(url, headers=current_headers, data=body)

            if response.status_code == 200:
                logger("Đã click quest: Retweet, Like and Comment - GDC Schedule")
            else:
                logger(f"Lỗi quest Retweet, Like and Comment - GDC Schedule: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi quest Retweet, Like and Comment - GDC Schedule: {str(e)}", 'error')

    async def quest_7117():
        try:
            url = 'https://hub.beamable.network/modules/questsold/7117'
            current_headers = headers.copy()
            current_headers["next-action"] = "eef77ac1785cc4d8ca64fb769a7cc5e0bc594592"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":7117,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":false,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like and Comment - GDC is Here^!","progress":1,"affirmType":{"questId":7117,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":7117,"link":"https://x.com/Beamable/status/1901677776819917239"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},1614,"questsold",true,false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã click quest: Retweet, Like and Comment - GDC is Here!")
            else:
                logger(f"Lỗi quest Retweet, Like and Comment - GDC is Here!: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi quest Retweet, Like and Comment - GDC is Here!: {str(e)}", 'error')

    async def quest_7081():
        try:
            url = 'https://hub.beamable.network/modules/questsold/7081'
            current_headers = headers.copy()
            current_headers["next-action"] = "eef77ac1785cc4d8ca64fb769a7cc5e0bc594592"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":7081,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":false,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like & Comment - Founder Introduction","progress":1,"affirmType":{"questId":7081,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":7081,"link":"https://x.com/jradoff/status/1900616630041817119"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},1614,"questsold",true,false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã click quest: Retweet, Like & Comment - Founder Introduction")
            else:
                logger(f"Lỗi quest: Retweet, Like & Comment - Founder Introduction: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi quest: Retweet, Like & Comment - Founder Introduction: {str(e)}", 'error')

    async def quest_7075():
        try:
            url = 'https://hub.beamable.network/modules/questsold/7075'
            current_headers = headers.copy()
            current_headers["next-action"] = "eef77ac1785cc4d8ca64fb769a7cc5e0bc594592"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":7075,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":false,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like and Comment - Evolution of Creator Economies","progress":1,"affirmType":{"questId":7075,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":7075,"link":"https://x.com/Beamablenetwork/status/1900532368693416167"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},1614,"questsold",true,false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã click quest: Retweet, Like and Comment - Evolution of Creator Economies")
            else:
                logger(f"Lỗi quest Retweet, Like and Comment - Evolution of Creator Economies: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi quest Retweet, Like and Comment - Evolution of Creator Economies: {str(e)}", 'error')

    async def quest_7069():
        try:
            url = 'https://hub.beamable.network/modules/questsold/7069'
            current_headers = headers.copy()
            current_headers["next-action"] = "eef77ac1785cc4d8ca64fb769a7cc5e0bc594592"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":7069,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":false,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like & Comment - First peek at Ninja Frog Gameplay","progress":1,"affirmType":{"questId":7069,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":7069,"link":"https://x.com/PlayPudgyParty/status/1900215815191859469"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},1614,"questsold",true,false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã click quest: Retweet, Like & Comment - First peek at Ninja Frog Gameplay")
            else:
                logger(f"Lỗi quest Retweet, Like & Comment - First peek at Ninja Frog Gameplay: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi quest Retweet, Like & Comment - First peek at Ninja Frog Gameplay: {str(e)}", 'error')

    async def quest_6975():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6975'
            current_headers = headers.copy()
            current_headers["next-action"] = "eef77ac1785cc4d8ca64fb769a7cc5e0bc594592"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6975,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":false,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like and Comment - See you soon WolvesDEN","progress":1,"affirmType":{"questId":6975,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6975,"link":"https://x.com/Beamablenetwork/status/1900328521840443409"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},1614,"questsold",true,false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã click quest: Retweet, Like and Comment - See you soon WolvesDEN")
            else:
                logger(f"Lỗi quest Retweet, Like and Comment - See you soon WolvesDEN: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi quest Retweet, Like and Comment - See you soon WolvesDEN: {str(e)}", 'error')

    async def quest_6973():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6973'
            current_headers = headers.copy()
            current_headers["next-action"] = "eef77ac1785cc4d8ca64fb769a7cc5e0bc594592"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6973,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":false,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like & Comment - Beamable and WolvesDAO at GDC","progress":1,"affirmType":{"questId":6973,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6973,"link":"https://x.com/Beamable/status/1900284795763974309"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},1614,"questsold",true,false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã click quest: Retweet, Like & Comment - Beamable and WolvesDAO at GDC")
            else:
                logger(f"Lỗi quest Retweet, Like & Comment - Beamable and WolvesDAO at GDC: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi quest Retweet, Like & Comment - Beamable and WolvesDAO at GDC: {str(e)}", 'error')

    async def quest_6956():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6956'
            current_headers = headers.copy()
            current_headers["next-action"] = "eef77ac1785cc4d8ca64fb769a7cc5e0bc594592"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6956,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":false,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like & Comment - Is This A Good Offer?","progress":1,"affirmType":{"questId":6956,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6956,"link":"https://x.com/Beamablenetwork/status/1899928563752853638"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},1614,"questsold",true,false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã click quest: Retweet, Like & Comment - Beamable Hub")
            else:
                logger(f"Lỗi quest Retweet, Like & Comment - Beamable Hub: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi quest Retweet, Like & Comment - Beamable Hub: {str(e)}", 'error')

    async def quest_6969():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6969'
            current_headers = headers.copy()
            current_headers["next-action"] = "eef77ac1785cc4d8ca64fb769a7cc5e0bc594592"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6969,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":false,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like & Comment - Beamable Hub","progress":1,"affirmType":{"questId":6969,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6969,"link":"https://x.com/Beamable/status/1900230776051908677"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},1614,"questsold",true,false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã click quest: Retweet, Like & Comment - Is This A Good Offer?")
            else:
                logger(f"Lỗi quest Retweet, Like & Comment - Is This A Good Offer: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi quest Retweet, Like & Comment - Is This A Good Offer: {str(e)}", 'error')

    async def quest_6955():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6955'
            current_headers = headers.copy()
            current_headers["next-action"] = "eef77ac1785cc4d8ca64fb769a7cc5e0bc594592"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6955,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":false,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like & Comment - Web3 Game Development Livestream","progress":1,"affirmType":{"questId":6955,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6955,"link":"https://x.com/jradoff/status/1899807546766213581"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},1614,"questsold",true,false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã click quest: Retweet, Like & Comment - Web3 Game Development Livestream")
            else:
                logger(f"Lỗi quest Retweet, Like & Comment - Web3 Game Development Livestream: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi quest Retweet, Like & Comment - Web3 Game Development Livestream: {str(e)}", 'error')

    async def quest_6948():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6948'
            current_headers = headers.copy()
            current_headers["next-action"] = "eef77ac1785cc4d8ca64fb769a7cc5e0bc594592"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6948,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":false,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like and Comment on our sponsorship post from WolvesDAO^!","progress":1,"affirmType":{"questId":6948,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6948,"link":"https://x.com/WolvesDAO/status/1899844715610353923"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},1614,"questsold",true,false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã click quest: Retweet, Like and Comment on our sponsorship post from WolvesDAO!")
            else:
                logger(f"Lỗi quest Retweet, Like and Comment on our sponsorship post from WolvesDAO: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi quest Retweet, Like and Comment on our sponsorship post from WolvesDAO: {str(e)}", 'error')

    async def quest_6933():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6933'
            current_headers = headers.copy()
            current_headers["next-action"] = "eef77ac1785cc4d8ca64fb769a7cc5e0bc594592"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6933,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":false,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like and Comment our latest tweet on Beamable Network","progress":1,"affirmType":{"questId":6933,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6933,"link":"https://x.com/Beamablenetwork/status/1899591317627494836"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},1614,"questsold",true,false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã click quest: Retweet, Like and Comment our latest tweet on Beamable Network")
            else:
                logger(f"Lỗi quest Retweet, Like and Comment our latest tweet on Beamable Network: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi quest Retweet, Like and Comment our latest tweet on Beamable Network: {str(e)}", 'error')

    async def quest_6904():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6904'
            current_headers = headers.copy()
            current_headers["next-action"] = "eef77ac1785cc4d8ca64fb769a7cc5e0bc594592"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6904,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":true,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like and Comment on our First Tweet on Beamable Network","progress":2,"affirmType":{"questId":6904,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6904,"link":"https://x.com/Beamablenetwork/status/1899226126352093354"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},1614,"questsold",true,false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã click quest: Retweet, Like and Comment on our First Tweet on Beamable Network")
            else:
                logger(f"Lỗi quest Retweet, Like and Comment on our First Tweet on Beamable Network: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi quest Retweet, Like and Comment on our First Tweet on Beamable Network: {str(e)}", 'error')

    async def quest_6866():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6866'
            current_headers = headers.copy()
            current_headers["next-action"] = "eef77ac1785cc4d8ca64fb769a7cc5e0bc594592"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6866,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":false,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like and Comment on our GDC Founders & Investors Brunch Tweet","progress":1,"affirmType":{"questId":6866,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6866,"link":"https://x.com/Beamable/status/1899175498913128509"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},1614,"questsold",true,false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã click quest: Retweet, Like and Comment on our GDC Founders & Investors Brunch Tweet")
            else:
                logger(f"Lỗi quest Retweet, Like and Comment on our GDC Founders & Investors Brunch Tweet: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi quest Retweet, Like and Comment on our GDC Founders & Investors Brunch Tweet: {str(e)}", 'error')

    async def quest_6840():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6840'
            current_headers = headers.copy()
            current_headers["next-action"] = "eef77ac1785cc4d8ca64fb769a7cc5e0bc594592"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6840,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":false,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like & Comment on our Dashboard Tweet","progress":1,"affirmType":{"questId":6840,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6840,"link":"https://x.com/Beamable/status/1897692463931740500"},"showDescription":false,"claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},1614,"questsold",true,false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã click quest: Retweet, Like & Comment on our Dashboard Tweet")
            else:
                logger(f"Lỗi quest Retweet, Like & Comment on our Dashboard Tweet: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi quest Retweet, Like & Comment on our Dashboard Tweet: {str(e)}", 'error')

    async def quest_in_future():
        try:
                get_quest = session.get("https://gist.githubusercontent.com/hthodev/d34feb751b2314dd8abdfa4f1b2b60a4/raw/beamable_quest.txt")
                logger("Đang kiểm tra có quest nào vừa thêm mới không?")
                res = get_quest.text
                
                if not res or res == 'none':
                    logger("Không có quest nào mới thêm vào")
                    return
                
                quests = res.strip().split('\n')
                for quest in quests:
                    quest = quest.strip()
                    if not quest:
                        continue
                        
                    quest_id = quest.split('||')[0]
                    body = quest.split('||')[1]
                    url = f'https://hub.beamable.network/modules/questsold/{quest_id}'
                    
                    current_headers = headers.copy()
                    current_headers["next-action"] = "eef77ac1785cc4d8ca64fb769a7cc5e0bc594592"
                    current_headers["Cookie"] = cookie
                    
                    response = session.post(url, headers=current_headers, data=body)
                    if response.status_code == 200:
                        logger(f"Đã click quest {quest_id} đã thêm mới vào")
                    else:
                        logger(f"Lỗi khi click quest {quest_id}: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi quest: {str(e)}", 'error')

    # Execute all quests in order
    await quest_7129()
    await quest_7117()
    await quest_7081()
    await quest_7075()
    await quest_7069()
    await quest_6975()
    await quest_6973()
    await quest_6956()
    await quest_6969()
    await quest_6955()
    await quest_6948()
    await quest_6933()
    await quest_6904()
    await quest_6866()
    await quest_6840()
    await quest_in_future()

async def complete_quest(cookie, session):
    async def quest_7129():
        try:
            url = 'https://hub.beamable.network/modules/questsold/7129'
            current_headers = headers.copy()
            current_headers["next-action"] = "bbbd8d0791d8eb36a310384fa0d2b41763f342ed"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":7129,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":true,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like and Comment - GDC Schedule","progress":2,"affirmType":{"questId":7129,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":7129,"link":"https://x.com/BeamableNetwork/status/1901989668947960223"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},{"modulePath":"questsold"},false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã claim quest: Retweet, Like and Comment - GDC Schedule", 'success')
            else:
                logger(f"Lỗi claim quest Retweet, Like and Comment - GDC Schedule: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi claim quest Retweet, Like and Comment - GDC Schedule: {str(e)}", 'error')

    async def quest_7117():
        try:
            url = 'https://hub.beamable.network/modules/questsold/7117'
            current_headers = headers.copy()
            current_headers["next-action"] = "bbbd8d0791d8eb36a310384fa0d2b41763f342ed"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":7117,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":true,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like and Comment - GDC is Here^!","progress":2,"affirmType":{"questId":7117,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":7117,"link":"https://x.com/Beamable/status/1901677776819917239"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},{"modulePath":"questsold"},false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã claim quest: Retweet, Like and Comment - GDC is Here!", 'success')
            else:
                logger(f"Lỗi claim quest Retweet, Like and Comment - GDC is Here: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi claim quest Retweet, Like and Comment - GDC is Here: {str(e)}", 'error')

    async def quest_7081():
        try:
            url = 'https://hub.beamable.network/modules/questsold/7081'
            current_headers = headers.copy()
            current_headers["next-action"] = "bbbd8d0791d8eb36a310384fa0d2b41763f342ed"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":7081,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":true,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like & Comment - Founder Introduction","progress":2,"affirmType":{"questId":7081,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":7081,"link":"https://x.com/jradoff/status/1900616630041817119"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},{"modulePath":"questsold"},false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã claim quest: Retweet, Like & Comment - Founder Introduction", 'success')
            else:
                logger(f"Lỗi claim quest Retweet, Like & Comment - Founder Introduction: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi claim quest Retweet, Like & Comment - Founder Introduction: {str(e)}", 'error')

    async def quest_7075():
        try:
            url = 'https://hub.beamable.network/modules/questsold/7075'
            current_headers = headers.copy()
            current_headers["next-action"] = "bbbd8d0791d8eb36a310384fa0d2b41763f342ed"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":7075,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":true,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like and Comment - Evolution of Creator Economies","progress":2,"affirmType":{"questId":7075,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":7075,"link":"https://x.com/Beamablenetwork/status/1900532368693416167"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},{"modulePath":"questsold"},false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã claim quest: Retweet, Like and Comment - Evolution of Creator Economies", 'success')
            else:
                logger(f"Lỗi claim quest Retweet, Like and Comment - Evolution of Creator Economies: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi claim quest Retweet, Like and Comment - Evolution of Creator Economies: {str(e)}", 'error')

    async def quest_7069():
        try:
            url = 'https://hub.beamable.network/modules/questsold/7069'
            current_headers = headers.copy()
            current_headers["next-action"] = "bbbd8d0791d8eb36a310384fa0d2b41763f342ed"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":7069,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":true,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like & Comment - First peek at Ninja Frog Gameplay","progress":2,"affirmType":{"questId":7069,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":7069,"link":"https://x.com/PlayPudgyParty/status/1900215815191859469"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},{"modulePath":"questsold"},false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã claim quest: Retweet, Like & Comment - First peek at Ninja Frog Gameplay", 'success')
            else:
                logger(f"Lỗi claim quest Retweet, Like & Comment - First peek at Ninja Frog Gameplay: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi claim quest Retweet, Like & Comment - First peek at Ninja Frog Gameplay: {str(e)}", 'error')

    async def quest_6975():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6975'
            current_headers = headers.copy()
            current_headers["next-action"] = "bbbd8d0791d8eb36a310384fa0d2b41763f342ed"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6975,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":true,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like and Comment - See you soon WolvesDEN","progress":2,"affirmType":{"questId":6975,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6975,"link":"https://x.com/Beamablenetwork/status/1900328521840443409"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},{"modulePath":"questsold"},false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã claim quest: Retweet, Like and Comment - See you soon WolvesDEN", 'success')
            else:
                logger(f"Lỗi claim quest Retweet, Like and Comment - See you soon WolvesDEN: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi claim quest Retweet, Like and Comment - See you soon WolvesDEN: {str(e)}", 'error')

    async def quest_6973():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6973'
            current_headers = headers.copy()
            current_headers["next-action"] = "bbbd8d0791d8eb36a310384fa0d2b41763f342ed"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6973,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":true,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like & Comment - Beamable and WolvesDAO at GDC","progress":2,"affirmType":{"questId":6973,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6973,"link":"https://x.com/Beamable/status/1900284795763974309"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},{"modulePath":"questsold"},false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã claim quest: Retweet, Like & Comment - Beamable and WolvesDAO at GDC", 'success')
            else:
                logger(f"Lỗi claim quest Retweet, Like & Comment - Beamable and WolvesDAO at GDC: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi claim quest Retweet, Like & Comment - Beamable and WolvesDAO at GDC: {str(e)}", 'error')

    async def quest_6956():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6956'
            current_headers = headers.copy()
            current_headers["next-action"] = "bbbd8d0791d8eb36a310384fa0d2b41763f342ed"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6956,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":true,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like & Comment - Is This A Good Offer?","progress":2,"affirmType":{"questId":6956,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6956,"link":"https://x.com/Beamablenetwork/status/1899928563752853638"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},{"modulePath":"questsold"},false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã claim quest: Retweet, Like & Comment - Beamable Hub", 'success')
            else:
                logger(f"Lỗi claim quest Retweet, Like & Comment - Beamable Hub: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi claim quest Retweet, Like & Comment - Beamable Hub: {str(e)}", 'error')

    async def quest_6969():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6969'
            current_headers = headers.copy()
            current_headers["next-action"] = "bbbd8d0791d8eb36a310384fa0d2b41763f342ed"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6969,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":true,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like & Comment - Beamable Hub","progress":2,"affirmType":{"questId":6969,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6969,"link":"https://x.com/Beamable/status/1900230776051908677"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},{"modulePath":"questsold"},false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã claim quest: Retweet, Like & Comment - Is This A Good Offer?", 'success')
            else:
                logger(f"Lỗi claim quest Retweet, Like & Comment - Is This A Good Offer: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi claim quest Retweet, Like & Comment - Is This A Good Offer: {str(e)}", 'error')

    async def quest_6955():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6955'
            current_headers = headers.copy()
            current_headers["next-action"] = "bbbd8d0791d8eb36a310384fa0d2b41763f342ed"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6955,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":true,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like & Comment - Web3 Game Development Livestream","progress":2,"affirmType":{"questId":6955,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6955,"link":"https://x.com/jradoff/status/1899807546766213581"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},{"modulePath":"questsold"},false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã claim quest: Retweet, Like & Comment - Web3 Game Development Livestream", 'success')
            else:
                logger(f"Lỗi claim quest Retweet, Like & Comment - Web3 Game Development Livestream: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi claim quest Retweet, Like & Comment - Web3 Game Development Livestream: {str(e)}", 'error')

    async def quest_6948():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6948'
            current_headers = headers.copy()
            current_headers["next-action"] = "bbbd8d0791d8eb36a310384fa0d2b41763f342ed"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6948,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":true,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like and Comment on our sponsorship post from WolvesDAO^!","progress":2,"affirmType":{"questId":6948,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6948,"link":"https://x.com/WolvesDAO/status/1899844715610353923"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},{"modulePath":"questsold"},false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã claim quest: Retweet, Like and Comment on our sponsorship post from WolvesDAO!", 'success')
            else:
                logger(f"Lỗi claim quest Retweet, Like and Comment on our sponsorship post from WolvesDAO: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi claim quest Retweet, Like and Comment on our sponsorship post from WolvesDAO: {str(e)}", 'error')

    async def quest_6933():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6933'
            current_headers = headers.copy()
            current_headers["next-action"] = "bbbd8d0791d8eb36a310384fa0d2b41763f342ed"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6933,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":true,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like and Comment our latest tweet on Beamable Network","progress":2,"affirmType":{"questId":6933,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6933,"link":"https://x.com/Beamablenetwork/status/1899591317627494836"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},{"modulePath":"questsold"},false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã claim quest: Retweet, Like and Comment our latest tweet on Beamable Network", 'success')
            else:
                logger(f"Lỗi claim quest Retweet, Like and Comment our latest tweet on Beamable Network: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi claim quest Retweet, Like and Comment our latest tweet on Beamable Network: {str(e)}", 'error')

    async def quest_6904():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6904'
            current_headers = headers.copy()
            current_headers["next-action"] = "bbbd8d0791d8eb36a310384fa0d2b41763f342ed"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6904,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":true,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like and Comment on our First Tweet on Beamable Network","progress":2,"affirmType":{"questId":6904,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6904,"link":"https://x.com/Beamablenetwork/status/1899226126352093354"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},{"modulePath":"questsold"},false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã claim quest: Retweet, Like and Comment on our First Tweet on Beamable Network", 'success')
            else:
                logger(f"Lỗi claim quest Retweet, Like and Comment on our First Tweet on Beamable Network: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi claim quest Retweet, Like and Comment on our First Tweet on Beamable Network: {str(e)}", 'error')

    async def quest_6866():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6866'
            current_headers = headers.copy()
            current_headers["next-action"] = "bbbd8d0791d8eb36a310384fa0d2b41763f342ed"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6866,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":true,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like and Comment on our GDC Founders & Investors Brunch Tweet","progress":2,"affirmType":{"questId":6866,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6866,"link":"https://x.com/Beamable/status/1899175498913128509"},"showDescription":false,"description":"ex. 'This quest is for x and y'","claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},{"modulePath":"questsold"},false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã claim quest: Retweet, Like and Comment on our GDC Founders & Investors Brunch Tweet", 'success')
            else:
                logger(f"Lỗi claim quest Retweet, Like and Comment on our GDC Founders & Investors Brunch Tweet: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi claim quest Retweet, Like and Comment on our GDC Founders & Investors Brunch Tweet: {str(e)}", 'error')

    async def quest_6840():
        try:
            url = 'https://hub.beamable.network/modules/questsold/6840'
            current_headers = headers.copy()
            current_headers["next-action"] = "bbbd8d0791d8eb36a310384fa0d2b41763f342ed"
            current_headers["Cookie"] = cookie
            
            body = """[{"questId":6840,"rewards":[{"resource":{"resourceId":4543,"projectId":80,"name":"Points","imageUrl":"https://cdn.harbor.gg/project/80/eee511fd8300e15e2997d773e8fba93c4d495516b64b58b181c202d3a02eef3d.png","description":"","longDescription":"","createdAt":"^$D2024-12-12T03:31:24.000Z"},"amount":500}],"questCompleted":true,"rewardClaimed":false,"questType":"ClickLink","questTypeName":"ClickLink","questName":"Retweet, Like & Comment on our Dashboard Tweet","progress":2,"affirmType":{"questId":6840,"affirm":"NonAffirmative"},"requires":0,"additional":{"questId":6840,"link":"https://x.com/Beamable/status/1897692463931740500"},"showDescription":false,"claimBehaviour":"ClaimThroughDetailsPage","detailsBehaviour":"DetailsPage","needsDetailsPage":true},{"modulePath":"questsold"},false]"""
            
            response = session.post(url, headers=current_headers, data=body)
            if response.status_code == 200:
                logger("Đã claim quest: Retweet, Like & Comment on our Dashboard Tweet", 'success')
            else:
                logger(f"Lỗi claim quest Retweet, Like & Comment on our Dashboard Tweet: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi claim quest Retweet, Like & Comment on our Dashboard Tweet: {str(e)}", 'error')

    async def quest_in_future():
        try:
                get_quest = session.get("https://gist.githubusercontent.com/hthodev/ce040c0cb8cc5a3e0a01b47556237225/raw/beamable_complete_quest.txt")
                res = get_quest.text
                if not res or res == 'none':
                    return
                
                quests = res.strip().split('\n')
                for quest in quests:
                    quest = quest.strip()
                    if not quest:
                        continue
                        
                    quest_id = quest.split('||')[0]
                    body = quest.split('||')[1]
                    url = f'https://hub.beamable.network/modules/questsold/{quest_id}'
                    
                    current_headers = headers.copy()
                    current_headers["next-action"] = "bbbd8d0791d8eb36a310384fa0d2b41763f342ed"
                    current_headers["Cookie"] = cookie
                    
                    response = session.post(url, headers=current_headers, data=body)
                    if response.status_code == 200:
                        logger(f"Đã claim quest {quest_id} đã thêm mới vào", 'success')
                    else:
                        logger(f"Lỗi khi claim quest {quest_id}: {response.status_code}", 'error')
        except Exception as e:
            logger(f"Lỗi claim quest: {str(e)}", 'error')

    # Execute all quests in order
    await quest_7129()
    await quest_7117()
    await quest_7081()
    await quest_7075()
    await quest_7069()
    await quest_6975()
    await quest_6973()
    await quest_6956()
    await quest_6969()
    await quest_6955()
    await quest_6948()
    await quest_6933()
    await quest_6904()
    await quest_6866()
    await quest_6840()
    await quest_in_future()


async def check_proxy_speed(proxy):
    start_time = time.time()
    scraper = create_scraper(proxy)
    test_url = "https://icanhazip.com/"
    
    try:
        response = scraper.get(test_url, timeout=5)
        elapsed_time = int((time.time() - start_time) * 1000)
        return {
            "status": "success",
            "time": elapsed_time,
            "statusCode": response.status_code,
            "proxy": proxy
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "proxy": proxy
        }

async def open_box(cookie, scraper):
    try:
        current_headers = headers.copy()
        current_headers["next-action"] = "7f1ddd18727e2bda9884d4f73c1ed2de315c9667cf"
        current_headers["Cookie"] = cookie
        
        response = scraper.post(
            "https://hub.beamable.network/modules/profile/5456",
            headers=current_headers,
            data="[5456,{\"path\":\"/profile/5456\"},1]"
        )
        
        if response.status_code == 200:
            logger("Đã mở hộp daily", "success")
        else:
            logger(f"Lỗi mở hộp daily: {response.status_code}", "error")
            
    except Exception as e:
        logger(f"Lỗi mở hộp daily: {str(e)}", "error")

async def get_nonce(cookie, scraper, retries=5, delay=1):
    for attempt in range(1, retries + 1):
        try:
            current_headers = headers.copy()
            current_headers["Cookie"] = cookie
            
            response = scraper.get(
                "https://hub.beamable.network/modules/aprildailies",
                headers=current_headers
            )

            if response.status_code == 200:
                text = response.text[-400000:]
                cleaned_text = text.replace('\\"', '"')
                
                pattern = re.compile(r'"nonce":"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})"')
                match = pattern.search(cleaned_text)
                
                if match:
                    return match.group(1)

        except Exception as e:
            logger(f"Lỗi get nonce (lần thử {attempt}): {str(e)}", "error")
        
        if attempt < retries:
            time.sleep(delay)

    return None

async def daily_check_in(cookie, scraper):
    try:
        nonce = await get_nonce(cookie, scraper)
        if not nonce:
            logger("Không thể lấy nonce", "error")
            return
            
        current_headers = headers.copy()
        current_headers["next-action"] = "7fb84504b1af6fa4a015452e147da5ba17d2d03551"
        current_headers["next-router-state-tree"] = "%5B%22%22%2C%7B%22children%22%3A%5B%5B%22host%22%2C%22hub.beamable.network%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22modules%22%2C%7B%22children%22%3A%5B%5B%22moduleIdOrPath%22%2C%22aprildailies%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fmodules%2Faprildailies%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D"
        current_headers["Cookie"] = cookie
        
        response = scraper.post(
            "https://hub.beamable.network/modules/aprildailies",
            headers=current_headers,
            data=f'[467,"{nonce}","aprildailies"]'
        )
        
        if response.status_code == 200:
            logger("Đã daily check-in thành công", "success")
            await open_box(cookie, scraper)
        elif response.status_code == 403:
            logger("Lỗi bị chặn do proxy nằm trong quốc gia bị chặn bởi dự án", "error")
        elif response.status_code == 504:
            logger("Server của dự án đang quá tải, thử lại sau 5 phút", "error")
            time.sleep(5 * 60)
            await daily_check_in(cookie, scraper)
        else:
            logger(f"Lỗi daily check-in: {response.status_code}", "error")
            
    except Exception as e:
        logger(f"Lỗi daily check-in: {str(e)}", "error")

async def process_account(cookie, proxy=None, do_task=True):
    try:
        scraper = create_scraper(proxy)
        
        if proxy:
            logger(f"Đang kiểm tra proxy {proxy}")
            proxy_check = await check_proxy_speed(proxy)
            logger(f"Proxy: {proxy} - Tốc độ: {proxy_check.get('time', 0)}ms - Status: {proxy_check.get('status', 'error')}")
        
        if do_task:
            await click_quest(cookie, scraper)
            logger("Chờ 1 chút để claim", "warn")
            time.sleep(10)
            await complete_quest(cookie, scraper)
        
        await daily_check_in(cookie, scraper)
        
    except Exception as e:
        logger(f"Lỗi xử lý tài khoản: {str(e)}", "error")

async def main():
    print("TOOL ĐƯỢC PHÁT TRIỂN BỞI: THIEN THO TRAN")
    print("Tham gia group facebook để nhận tool mới: https://www.facebook.com/groups/2072702003172443/")
    print("------------------------------------------------------------")
    
    do_task = input('Bạn có muốn làm task không, hay chỉ daily mỗi ngày? (y/n): ').lower() == 'y'
    
    while True:
        proxies, cookies = read_files()
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = []
            for i, cookie in enumerate(cookies):
                proxy = proxies[i] if i < len(proxies) else None
                futures.append(executor.submit(lambda: asyncio.run(process_account(cookie, proxy, do_task))))
            
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    logger(f"Lỗi trong quá trình xử lý: {str(e)}", "error")
        
        logger("Chờ 6 tiếng để tiếp tục daily", "warn")
        time.sleep(6 * 60 * 60)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
