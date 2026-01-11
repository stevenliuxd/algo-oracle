import yfinance as yf
import torch

def check_gpu():
    if torch.cuda.is_available():
        print(f"✅ GPU Found: {torch.cuda.get_device_name(0)}")
    else:
        print("❌ GPU NOT FOUND. Running on CPU.")

def get_data(ticker="NVDA"):
    print(f"Fetching data for {ticker}...")
    data = yf.download(ticker, period="1y")
    return torch.tensor(data['Close'].values).float().to('cuda')

if __name__ == "__main__":
    check_gpu()
    
    # Prove the GPU is working by running a "prediction" calculation
    # We move the stock prices to the GPU (cuda)
    prices = get_data("NVDA")
    
    # Simple AI Placeholder: Matrix multiplication on GPU
    # (In a real project, you'd load an LSTM or Transformer model here)
    weights = torch.randn(len(prices), len(prices)).to('cuda')
    analysis = torch.matmul(weights, prices)
    
    print(f"Analysis complete. Result vector size: {analysis.shape}")
    print("Top 5 AI-transformed values:", analysis[:5])
