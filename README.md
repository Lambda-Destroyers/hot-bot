# Team: Jared Ciccarello, Andrew Carroll, Slava Makeev


## Name of Project: Hot Bot

### Summary of idea: Create a crypto bot with AI.

  Monitoring crypto markets efficiently is a very time consuming investment strategy.  By creating an automated process with strong
  trading algorithms we hope to show a +5% return when processing historic data.  Should we accomplish this we will then set the bot loose

  in a test environment with fake funds but real time pricing data.



### Minimum Viable Product (MVP) definition.

Our MVP is a crypto bot that can show an ROI > current CD rates, savings accounts, and typical prospectus 
returns in the stock exchange.

**MetaTrader is a resource that Roger recommends.  Buy and sell in a fake environment!

## Domain model
![87c44fdbb55f0abd3d6841e2a1a690c3](https://github.com/Lambda-Destroyers/hot-bot/assets/71305940/bb956190-6b72-47dc-9839-5ab47c6b31a5)

## Wireframe
![b3be7ca5dcf55e128df84933e8204f13](https://github.com/Lambda-Destroyers/hot-bot/assets/71305940/c1fd4bf3-ea9a-465d-b8ef-d32d6d8fa488)


Advanced Trade API

Get started:
  pip or pip3
python3 -m venv .venv
pip3 install rich --- Library that allows you to create visually appealing and interactive text-based interfaces in the terminal.
pip3 install requests --- This allows for requests from API
pip3 install matplotlib --- library for creating charts
pip3 install pytest-cov --- This is for coverage testing
pip3 install openapi --- chatGPT api + API key


Look at main features of rich:
python3/python -m rich

Run file:
python3/python filename.py

Test Coverage: 
pytest --cov tests/


Advanced Trade API Docs
https://docs.cloud.coinbase.com/advanced-trade-api/docs/welcome

ChatGPT API Docs
https://platform.openai.com/docs/api-reference/introduction