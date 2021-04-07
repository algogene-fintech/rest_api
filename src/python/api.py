# -*- coding: utf-8 -*-

import requests
from datetime import datetime



class api:
    def __init__(self, user, api_key):
        self._user = str(user)
        self._api_key = str(api_key)
        self._base_url = "https://algogene.com/rest/v1/"
        self._timeout = 10
        self._session_token = ""
        self._session_expiry = ""

    def session(self):
        try:
            url = self._base_url+"session"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            if r.status_code==200:
                j = r.json()
                self._session_token = str(j["res"]["token"])
                self._session_expiry = datetime.strptime(str(j["res"]["expired_utc"]), "%Y-%m-%d %H:%M:%S.%f")
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}
    
    def renew_session(self):
        if self._session_token=="" or (self._session_expiry!="" and datetime.utcnow()>self._session_expiry):
            self.session()

    def accounts(self, runmode):
        try:
            self.renew_session()

            url = self._base_url+"accounts"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "runmode": str(runmode),
                "token": self._session_token
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def positions(self, runmode, accountid):
        try:
            self.renew_session()

            url = self._base_url+"positions"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "token": self._session_token,
                "runmode": str(runmode),
                "accountid": str(accountid)
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def balance(self, runmode, accountid):
        try:
            self.renew_session()

            url = self._base_url+"balance"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "token": self._session_token,
                "runmode": str(runmode),
                "accountid": str(accountid)
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def opened_trades(self, runmode, accountid):
        try:
            self.renew_session()

            url = self._base_url+"opened_trades"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "token": self._session_token,
                "runmode": str(runmode),
                "accountid": str(accountid)
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def pending_trades(self, runmode, accountid):
        try:
            self.renew_session()

            url = self._base_url+"pending_trades"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "token": self._session_token,
                "runmode": str(runmode),
                "accountid": str(accountid)
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def config(self, runmode, accountid, broker_info):
        try:
            self.renew_session()

            url = self._base_url+"config"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "token": self._session_token,
                "runmode": str(runmode),
                "accountid": str(accountid)
            }
            if "broker_name" in broker_info: 
                data["broker_name"] = str(broker_info["broker_name"])
            if "broker_api" in broker_info: 
                data["broker_api"] = str(broker_info["broker_api"])
            if "broker_account" in broker_info: 
                data["broker_account"] = str(broker_info["broker_account"])
            if "broker_account_type" in broker_info: 
                data["broker_account_type"] = str(broker_info["broker_account_type"])
            if "broker_user" in broker_info: 
                data["broker_user"] = str(broker_info["broker_user"])
            if "broker_pwd" in broker_info: 
                data["broker_pwd"] = str(broker_info["broker_pwd"])
            if "broker_server" in broker_info: 
                data["broker_server"] = str(broker_info["broker_server"])
            r = requests.request("post", url, json=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def close_orders(self, runmode, accountid, tradeIDs):
        try:
            self.renew_session()

            url = self._base_url+"close_orders"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "token": self._session_token,
                "runmode": str(runmode),
                "accountid": str(accountid),
                "tradeIDs": str(tradeIDs)
            }
            r = requests.request("post", url, json=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def cancel_orders(self, runmode, accountid, tradeIDs):
        try:
            self.renew_session()

            url = self._base_url+"cancel_orders"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "token": self._session_token,
                "runmode": str(runmode),
                "accountid": str(accountid),
                "tradeIDs": str(tradeIDs)
            }
            r = requests.request("post", url, json=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def update_opened_order(self, runmode, accountid, tradeID, callback="", orderRef="", takeProfitLevel=-1, stopLossLevel=-1, holdtime=-1):
        try:
            self.renew_session()

            url = self._base_url+"update_opened_order"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "token": self._session_token,
                "runmode": str(runmode),
                "accountid": str(accountid),
                "tradeID": str(tradeID)
            }
            if callback!="": 
                data["callback"] = str(callback)
            if orderRef!="": 
                data["orderRef"] = str(orderRef)
            if takeProfitLevel!=-1: 
                data["takeProfitLevel"] = float(takeProfitLevel)
            if stopLossLevel!=-1: 
                data["stopLossLevel"] = float(stopLossLevel)
            if holdtime!=-1: 
                data["holdtime"] = int(holdtime)
            r = requests.request("post", url, json=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def update_pending_order(self, runmode, accountid, tradeID, callback="", orderRef="", takeProfitLevel=-1, stopLossLevel=-1, holdtime=-1, price=-1, timeinforce=-1):
        try:
            self.renew_session()

            url = self._base_url+"update_pending_order"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "token": self._session_token,
                "runmode": str(runmode),
                "accountid": str(accountid),
                "tradeID": str(tradeID)
            }
            if callback!="": 
                data["callback"] = str(callback)
            if orderRef!="": 
                data["orderRef"] = str(orderRef)
            if takeProfitLevel!=-1: 
                data["takeProfitLevel"] = float(takeProfitLevel)
            if stopLossLevel!=-1: 
                data["stopLossLevel"] = float(stopLossLevel)
            if holdtime!=-1: 
                data["holdtime"] = int(holdtime)
            if price!=-1: 
                data["price"] = float(price)
            if timeinforce!=-1: 
                data["timeinforce"] = int(timeinforce)
            r = requests.request("post", url, json=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def open_order(self, runmode, accountid, instrument, expiry="", right="", strike=0, buysell="", volume=0, ordertype="", callback="", orderRef="", takeProfitLevel=-1, stopLossLevel=-1, holdtime=-1, price=-1, timeinforce=-1):
        try:
            self.renew_session()

            url = self._base_url+"open_order"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "token": self._session_token,
                "runmode": str(runmode),
                "accountid": str(accountid),
                "instrument": str(instrument)
            }
            if expiry!="": 
                data["expiry"] = str(expiry)
            if right!="": 
                data["right"] = str(right)
            if strike!=0: 
                data["strike"] = float(strike)
            if buysell!="": 
                data["buysell"] = str(buysell)
            if volume!=0: 
                data["volume"] = float(volume)
            if ordertype!="": 
                data["ordertype"] = str(ordertype)
            if callback!="": 
                data["callback"] = str(callback)
            if orderRef!="": 
                data["orderRef"] = str(orderRef)
            if takeProfitLevel!=-1: 
                data["takeProfitLevel"] = float(takeProfitLevel)
            if stopLossLevel!=-1: 
                data["stopLossLevel"] = float(stopLossLevel)
            if holdtime!=-1: 
                data["holdtime"] = int(holdtime)
            if price!=-1: 
                data["price"] = float(price)
            if timeinforce!=-1: 
                data["timeinforce"] = int(timeinforce)
            r = requests.request("post", url, json=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def history_price(self, instrument, count, interval, timestamp, expiry="", right="", strike=0):
        try:
            url = self._base_url+"history_price"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "instrument": str(instrument),
                "count": int(count),
                "interval": str(interval),
                "timestamp": str(timestamp)
            }
            if expiry!="":
                data["expiry"] = expiry
            if right!="":
                data["right"] = right
            if strike!=0:
                data["strike"] = strike
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def history_news(self, lang, count, starttime, endtime):
        try:
            url = self._base_url+"history_news"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "lang": str(lang),
                "count": int(count),
                "starttime": str(starttime),
                "endtime": str(endtime)
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def history_weather(self, city, starttime, endtime):
        try:
            url = self._base_url+"history_weather"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "city": str(city),
                "starttime": str(starttime),
                "endtime": str(endtime)
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def history_econs_calendar(self, starttime, endtime):
        try:
            url = self._base_url+"history_econs_calendar"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "starttime": str(starttime),
                "endtime": str(endtime)
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def history_econs_stat(self, series_id, starttime, endtime):
        try:
            url = self._base_url+"history_econs_stat"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "series_id": str(series_id),
                "starttime": str(starttime),
                "endtime": str(endtime)
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def list_instrument(self):
        try:
            url = self._base_url+"list_instrument"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def meta_instrument(self, instrument):
        try:
            url = self._base_url+"meta_instrument"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "instrument": str(instrument)
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def list_econs_series(self):
        try:
            url = self._base_url+"list_econs_series"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def meta_econs_series(self, series_id):
        try:
            url = self._base_url+"meta_econs_series"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "series_id": str(series_id)
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def realtime_price(self, symbols):
        try:
            url = self._base_url+"realtime_price"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "symbols": str(symbols)
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def realtime_news(self, lang):
        try:
            url = self._base_url+"realtime_news"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "lang": str(lang)
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def realtime_econs_stat(self):
        try:
            url = self._base_url+"realtime_econs_stat"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def realtime_weather(self, city):
        try:
            url = self._base_url+"realtime_weather"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "city": str(city)
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def realtime_exchange_rate(self, cur1, cur2):
        try:
            url = self._base_url+"realtime_exchange_rate"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "cur1": str(cur1),
                "cur2": str(cur2)
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def realtime_econs_calendar(self):
        try:
            url = self._base_url+"realtime_econs_calendar"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def strategy_stats(self, runmode, runtime_id, acdate=""):
        try:
            url = self._base_url+"strategy_stats"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "runmode": str(runmode),
                "runtime_id": str(runtime_id)
            }
            if acdate!="":
                data["acdate"] = str(acdate)
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def strategy_pl(self, runmode, runtime_id, acdate=""):
        try:
            url = self._base_url+"strategy_pl"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "runmode": str(runmode),
                "runtime_id": str(runtime_id)
            }
            if acdate!="":
                data["acdate"] = str(acdate)
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def strategy_pos(self, runmode, runtime_id, acdate=""):
        try:
            url = self._base_url+"strategy_pos"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "runmode": str(runmode),
                "runtime_id": str(runtime_id)
            }
            if acdate!="":
                data["acdate"] = str(acdate)
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def strategy_bal(self, runmode, runtime_id, acdate=""):
        try:
            url = self._base_url+"strategy_bal"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "runmode": str(runmode),
                "runtime_id": str(runtime_id)
            }
            if acdate!="":
                data["acdate"] = str(acdate)
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def strategy_trade(self, runmode, runtime_id, acdate=""):
        try:
            url = self._base_url+"strategy_trade"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "runmode": str(runmode),
                "runtime_id": str(runtime_id)
            }
            if acdate!="":
                data["acdate"] = str(acdate)
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

    def strategy_market_perf(self, symbol, startDate, endDate):
        try:
            url = self._base_url+"strategy_market_perf"
            headers = {'Content-Type': 'application/json'}
            data = {
                "user": self._user,
                "api_key": self._api_key,
                "runmode": str(runmode),
                "symbol": str(symbol),
                "startDate": str(startDate),
                "endDate": str(endDate)
            }
            r = requests.request("get", url, params=data, headers=headers, timeout=self._timeout)
            return r.status_code, r.json()
        except Exception as e:
            return 400, {}

