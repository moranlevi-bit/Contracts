# Contracts
AI Powered Contract Management

## Contract data table

`extract_contracts.py` reads every contract (`.pdf`, `.docx`, `.txt`) in a folder,
uses Claude to extract the fields below, and writes one row per contract to Excel or CSV.

| Column   | What is collected                                        |
|----------|----------------------------------------------------------|
| File     | Contract file name                                       |
| Org Name | Organization / company party to the contract             |
| Industry | The organization's industry or sector                    |
| Earnings | Base pay, salary, fees or contract value (amount, currency, period) |
| Bonuses  | Bonuses, commissions, incentives (amounts and conditions) |

Fields the contract doesn't contain are left blank.

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...        # or `ant auth login`
python extract_contracts.py contracts/ -o contracts_table.xlsx   # or .csv
```

A sample contract is in `contracts/`.
