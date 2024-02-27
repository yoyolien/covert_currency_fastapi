# 匯率轉換 API

## 簡介

此 API 提供一個簡單的匯率轉換服務，讓使用者能夠根據提供的匯率將金額從一種貨幣轉換為另一種。

## 功能

- **GET url:** `/`
    - 接受源貨幣 (`source`)、目標貨幣 (`target`) 和金額 (`amount`) 參數。
    - 將給定的金額從源貨幣轉換為目標貨幣。
    - 返回轉換後的金額。

## 使用方式

### 請求

範例：

```bash
curl -X 'GET' \
  'http://localhost:8000/?source=USD&target=JPY&amount=$1,525' \
  -H 'accept: application/json'
```

### 回應

```json
{
  "message": "success",
  "amount": "$170,496.53"
}
```

### 安裝與執行

1. clone

```bash
  git clone https://github.com/yoyolien/covert_currency_fastapi
```

2. 安裝相關套件

```bash
  pip install -r requirement.txt
```

3. 執行

```bash
  uvicorn main:app --reload
```



