import algogene
ag = algogene.api(user="user", api_key="xxxxxxxxxxxxxxxxxxxxxxxx")

print(ag.session())
print(ag.accounts(runmode="livetest"))
print(ag.positions(runmode="livetest", accountid="1000"))
print(ag.balance(runmode="livetest", accountid="1000"))
print(ag.opened_trades(runmode="livetest", accountid="1000"))
print(ag.pending_trades(runmode="livetest", accountid="1000"))
print(ag.config(runmode="livetest", accountid="1000", broker_info={"broker_name":"oanda","broker_api":"xxxxxx"} ))


print(ag.close_orders(runmode="livetest", accountid="1000", tradeIDs="192,193,194"))
print(ag.cancel_orders(runmode="livetest", accountid="1000", tradeIDs="192,193,194"))
print(ag.update_opened_order(runmode="livetest", accountid="1000", tradeID=12, takeProfitLevel=150))
print(ag.update_pending_order(runmode="livetest", accountid="1000", tradeID=12, price=90))
print(ag.open_order(runmode="livetest", accountid="1000", instrument="EURUSD", buysell="BUY", volume=0.01, ordertype="MKT", stopLossLevel=1.05, orderRef="my order abcd1234"))


print(ag.history_price(instrument="USDJPY", count=100, interval="D", timestamp="2020-10-30 00:00:00"))
print(ag.history_news(lang='en', count=5, starttime='2021-03-22', endtime='2021-03-22'))
print(ag.history_weather(city='Tokyo', starttime='2021-03-25', endtime='2021-03-25'))
print(ag.history_econs_calendar(starttime='2021-03-01', endtime='2021-03-05'))
print(ag.history_econs_stat(series_id="YOUN639TRADN", starttime='2020-01-01', endtime='2020-05-31'))


print(ag.list_instrument())
print(ag.meta_instrument(instrument="USDJPY"))
print(ag.list_econs_series())
print(ag.meta_econs_series(series_id="REALGDPSERV56041"))


print(ag.realtime_price(symbols="HKXHKD,SPXUSD"))
print(ag.realtime_news(lang="ko"))
print(ag.realtime_econs_stat())
print(ag.realtime_weather(city="Beijing"))
print(ag.realtime_exchange_rate(cur1="HKD", cur2="JPY"))
print(ag.realtime_econs_calendar())


print(ag.strategy_stats(runmode="livetest", runtime_id="1000", acdate=""))
print(ag.strategy_pl(runmode="livetest", runtime_id="1000", acdate=""))
print(ag.strategy_pos(runmode="livetest", runtime_id="1000", acdate=""))
print(ag.strategy_bal(runmode="livetest", runtime_id="1000", acdate=""))
print(ag.strategy_trade(runmode="livetest", runtime_id="1000", acdate="2021-04-01"))
print(ag.strategy_market_perf(symbol="AUXAUD", startDate="2019-01-01", endDate="2019-12-31"))
