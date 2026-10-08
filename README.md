# my_chess_com
Just testing the limitations of what I can and can't do with Chess.com's public API. ♟️🙂

## Test Site
Refer to this [site](https://c-cread.github.io/my_chess_com/) to view my profile and other popular chess players. 

<img width="1043" height="787" alt="image" src="https://github.com/user-attachments/assets/eb837e45-c3e6-4f35-87c1-6bad68f64037" />

## C-CREAD's Overview 
Using basic API endpoints to get my stats from rapid, blitz, and bullet games. 
### Overview 
| Rating | Wins ➕ | Losses ➖ | Draws 🟰 |
| :-----------------: | :-----------------: | :-----------------: | :-----------------: | 
| ![Rapid](https://img.shields.io/badge/dynamic/json?url=https://api.chess.com/pub/player/c-cread/stats&query=$.chess_rapid.last.rating&label=Rapid&logo=chessdotcom&color=769656) | ![Wins](https://img.shields.io/badge/dynamic/json?url=https://api.chess.com/pub/player/c-cread/stats&query=$.chess_rapid.record.win&label=Wins&color=769656) | ![Losses](https://img.shields.io/badge/dynamic/json?url=https://api.chess.com/pub/player/c-cread/stats&query=$.chess_rapid.record.loss&label=Losses&color=769656) |![Draws](https://img.shields.io/badge/dynamic/json?url=https://api.chess.com/pub/player/c-cread/stats&query=$.chess_rapid.record.draw&label=Draws&color=769656) |
| ![Blitz](https://img.shields.io/badge/dynamic/json?url=https://api.chess.com/pub/player/c-cread/stats&query=$.chess_blitz.last.rating&label=Blitz&logo=chessdotcom&color=F7C843) | ![Wins](https://img.shields.io/badge/dynamic/json?url=https://api.chess.com/pub/player/c-cread/stats&query=$.chess_blitz.record.win&label=Wins&color=F7C843) | ![Losses](https://img.shields.io/badge/dynamic/json?url=https://api.chess.com/pub/player/c-cread/stats&query=$.chess_blitz.record.loss&label=Losses&color=F7C843) | ![Draws](https://img.shields.io/badge/dynamic/json?url=https://api.chess.com/pub/player/c-cread/stats&query=$.chess_blitz.record.draw&label=Draws&color=F7C843) |
| ![Bullet](https://img.shields.io/badge/dynamic/json?url=https://api.chess.com/pub/player/c-cread/stats&query=$.chess_bullet.last.rating&label=Bullet&logo=chessdotcom&color=E8751A) | ![Wins](https://img.shields.io/badge/dynamic/json?url=https://api.chess.com/pub/player/c-cread/stats&query=$.chess_bullet.record.win&label=Wins&color=E8751A) | ![Losses](https://img.shields.io/badge/dynamic/json?url=https://api.chess.com/pub/player/c-cread/stats&query=$.chess_bullet.record.loss&label=Losses&color=E8751A) | ![Draws](https://img.shields.io/badge/dynamic/json?url=https://api.chess.com/pub/player/c-cread/stats&query=$.chess_bullet.record.draw&label=Draws&color=E8751A) |
