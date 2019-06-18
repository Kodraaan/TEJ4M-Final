## Transaction Message Breakdown (BIG ENDIAN)
| Name           | Size (bits, unsigned) |
| -------------- |:-----------:|
| Transaction ID | 32 |
| Sender Address | 64 |
| Receipient Address | 64 |
| Sender IP      | 32 |
| Transaction Amount | 32 |
| Sender Balance | 32 |
| Sender Public Key | 1024 |
| Digital Signature | 64 |
|||
| **TOTAL** | 1344 |

## Block Breakdown (BIG ENDIAN)
| Name | Size (bits, unsigned) |
| -- |:--:|
| Block ID | 32 |
| Previous Block Hash | 160 |
| Transactions | 1344x10=13440 |
| Miner Reward | 64+8 |
| Number of Wallets | 32 |
| Account Balances (n users) | (64+32) x n |
| Proof of Work Padding | 160 |
|||
| **TOTAL** | 13896+32x64 |