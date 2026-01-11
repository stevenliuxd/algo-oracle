FROM cuda-nightly

WORKDIR /app

COPY requirements.txt analyze_stocks.py .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "analyze_stocks.py"]
