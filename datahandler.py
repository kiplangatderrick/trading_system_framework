from dataclasses import dataclass
import pandas as pd
from typing import Callable, List

@dataclass
class MarketData:
    symbol: str
    data: pd.DataFrame
    
    def add_column(self, name: str, func: Callable[[pd.DataFrame], pd.Series]):
        self.data[name] = func(self.data)
        
    def filter(self, condition: Callable[[pd.DataFrame], pd.Series]):
        self.data = self.data[condition(self.data)]
        
        
def compute_returns(df: pd.DataFrame) -> pd.Series:
    return df["price"].pct_change()

def moving_average(window: int) -> Callable:
    def _ma(df: pd.DataFrame) -> pd.Series:
        return df["price"].rolling(window).mean()
    return _ma

def pipeline(data: MarketData, steps: List[Callable[[MarketData], None]]):
    for step in steps:
        step(data)
    return data


if __name__ == "__main__":
    df = pd.DataFrame({
        "price": [100, 101, 102, 101, 105]
    })
    market_data = MarketData(symbol="AAPL", data=df)
    steps = [
        lambda d: d.add_column("returns", compute_returns),
        lambda d: d.add_column("ma_3", moving_average(3)),
        lambda d: d.filter(lambda df: df["returns"].notna())
    ]
    
result = pipeline(market_data, steps)
print(result.data)