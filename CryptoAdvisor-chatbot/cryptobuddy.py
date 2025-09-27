#!/usr/bin/env python3
# CryptoBuddy - Rule-based Cryptocurrency Advisor Chatbot

from typing import Dict

# Predefined cryptocurrency dataset
crypto_db = {
    "Bitcoin": {
        "symbol": "BTC",
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "symbol": "ETH",
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "symbol": "ADA",
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    },
    "Algorand": {
        "symbol": "ALGO",
        "price_trend": "falling",
        "market_cap": "low",
        "energy_use": "low",
        "sustainability_score": 9/10
    }
}

class CryptoBuddy:
    def __init__(self, name="CryptoBuddy", tone="friendly"):
        self.name = name
        self.tone = tone
        self.disclaimer = ("I am a simple rule-based advisor. Crypto is risky—always do your own research. "
                           "This is not financial advice.")

    def reply(self, user_query: str) -> str:
        q = user_query.lower().strip()
        # Intent detection via keywords
        if any(x in q for x in ["sustain", "eco", "green", "environment"]):
            return self._most_sustainable()
        if any(x in q for x in ["trend", "trending", "up", "rising", "growth", "grow"]):
            return self._trending_up()
        if any(x in q for x in ["buy", "recommend", "should i", "invest"]):
            return self._recommend_for_investment(q)
        if "help" in q or "how" in q:
            return self._help_text()
        if "list" in q or "show" in q or "coins" in q:
            return self._list_coins()
        return ("Sorry, I didn't understand. Try asking: 'Which crypto is trending up?' "
                "or 'What's the most sustainable coin?'")

    def _most_sustainable(self) -> str:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        score = crypto_db[recommend]["sustainability_score"]
        return (f"🌱 Most sustainable: {recommend} ({crypto_db[recommend]['symbol']}). "
                f"Sustainability score: {score:.1f}/10. Energy use: {crypto_db[recommend]['energy_use']}. "
                f"{self.disclaimer}")

    def _trending_up(self) -> str:
        rising = [coin for coin, d in crypto_db.items() if d["price_trend"] == "rising"]
        if not rising:
            return "No coins are currently marked as 'rising' in my dataset."
        # Prefer higher market cap
        mapping = {"low": 1, "medium": 2, "high": 3}
        best = max(rising, key=lambda c: mapping[crypto_db[c]["market_cap"]])
        d = crypto_db[best]
        return (f"🚀 Trending: {best} ({d['symbol']}) is trending up with market cap {d['market_cap']}. "
                f"Energy use: {d['energy_use']}. {self.disclaimer}")

    def _recommend_for_investment(self, q: str) -> str:
        if "long" in q or "long-term" in q:
            # Rising trend + high sustainability
            candidates = [c for c, d in crypto_db.items()
                          if d["price_trend"] == "rising" and d["sustainability_score"] > 7/10]
            if candidates:
                best = candidates[0]
                return (f"{best} ({crypto_db[best]['symbol']}) is a good long-term pick: "
                        f"rising trend and sustainability score {crypto_db[best]['sustainability_score']:.1f}/10. "
                        f"{self.disclaimer}")
            # fallback: highest market cap among rising coins
            candidates = [c for c, d in crypto_db.items() if d["price_trend"] == "rising"]
            if candidates:
                mapping = {"low": 1, "medium": 2, "high": 3}
                best = max(candidates, key=lambda c: mapping[crypto_db[c]["market_cap"]])
                return (f"{best} ({crypto_db[best]['symbol']}) is trending and may suit long-term growth. "
                        f"Sustainability score: {crypto_db[best]['sustainability_score']:.1f}/10. "
                        f"{self.disclaimer}")
            return "I don't have a clear long-term candidate. Try asking about sustainability or trend."
        # Default recommendation: score by trend + sustainability + market cap
        def coin_score(d: Dict) -> float:
            trend_score = {"rising": 2, "stable": 1, "falling": 0}
            market_score = {"low": 0.5, "medium": 1, "high": 1.5}
            return trend_score.get(d["price_trend"], 0) + d["sustainability_score"] + market_score.get(d["market_cap"], 0)
        best = max(crypto_db, key=lambda c: coin_score(crypto_db[c]))
        d = crypto_db[best]
        return (f"My simple pick: {best} ({d['symbol']}). Trend: {d['price_trend']}, market cap: {d['market_cap']}, "
                f"sustainability: {d['sustainability_score']:.1f}/10. {self.disclaimer}")

    def _help_text(self) -> str:
        return ("I can answer: 'Which crypto is trending up?', 'What's the most sustainable coin?', "
                "'Which coin should I buy?', 'List coins'. Try: 'Which crypto should I buy for long-term growth?'")

    def _list_coins(self) -> str:
        lines = [f"{name} ({d['symbol']}): trend={d['price_trend']}, market_cap={d['market_cap']}, sustainability={d['sustainability_score']:.1f}/10"
                 for name, d in crypto_db.items()]
        return "Coins in my dataset:\n" + "\n".join(lines)


# Demo run
if __name__ == "__main__":
    bot = CryptoBuddy()
    print("Welcome to CryptoBuddy! Type your questions or 'exit' to quit.")
    while True:
        user_query = input("You: ")
        if user_query.lower() in ("exit", "quit"):
            print("CryptoBuddy: Goodbye! 🌟")
            break
        response = bot.reply(user_query)
        print("CryptoBuddy:", response)
        print("-" * 60)

