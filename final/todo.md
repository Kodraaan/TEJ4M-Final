## Transaction Message Breakdown (BIG ENDIAN)
| Name           | Size (bits) |
| -------------- |:-----------:|
| Transaction ID | u32 |
| Sender Address | 64 |
| Receipient Address | 64 |
| Sender IP      | 32 |
| Transaction Amount | u32 |
| Sender Balance | u32 |
| Sender Public Key | 1024 |
| Digital Signature | 56 |
|||
| **TOTAL** | 1336 |

## Block Breakdown (BIG ENDIAN)
| Name | Size (bits) |
| -- |:--:|
| Block ID | u32 |
| Previous Block Hash | 160 |
| Transactions | 1336x10=13360 |
| Miner Reward | 64+u8 |
| Number of Wallets | u32 |
| Account Balances (n users) | (u32+64) x n |
| Proof of Work Padding | 160 |
|||
| **TOTAL** | 13816+32x64 |