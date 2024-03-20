# MAP BASE
"""

level_map_X: list[str] = [
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS      BACKLW",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S    I  G                                                  S",
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",
]

"""

level_map_1: list[str] = [
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S       E                 A            K                   S",
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSWWSSSSSSSSSSSSS          S",
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S    I  G                              B                   S",
"SSSSSSSSSSSSSSSSSSSSSSWWSSSSSWWSSSSSSSSSSSSSSSSSSSSSLLLSSSSS",
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",
]

level_map_2: list[str] = [
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS                                           BACKLW",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                            SSSSSSSSSSSSSSSSSSSSSSSS      S",
"S                                     SSS                  S",
"S                                     SSS                  S",
"S                                     SSS              SSSSS",
"S                                     SSS                  S",
"S                                     SSS                  S",
"S                                     SSS            SSSSSSS",
"S                                     SSS                  S",
"S                                     SSS                  S",
"S                                     SSSSSSSSSS           S",
"S                                     SSS                  S",
"S                                     SSS                  S",
"S                                     SSS            SSSSSSS",
"S                                     SSS                  S",
"S                                     SSS                  S",
"SSSSSSSSSSSSSSSSSSSSS                 SSSSSSSSSS           S",
"S                                                          S",
"S                                                          S",
"S                                                    SSSSSSS",
"S                                                          S",
"S    I  G                                                  S",
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",
]

level_map_3: list[str] = [
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS      BACKLW",
"S                                                         S",
"S                                   L                      S",
"S                             B          B                 S",
"S              SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS    S",
"S              S                                       S   S",
"S              S                                           S",
"S      K       S    SSS                                    S",
"S   SSSSSSSSSSSS    S S                                    S",
"S              S    S S               K                   SS",
"S              S    S S          SSSSSSSSSSS               S",
"S              S    S S                                    S",
"S              S    S S                                    S",
"S              S    S S                                   BS",
"S              S    S SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS     SSS",
"S              S    S                              S       S",
"S              S    S                              S       S",
"S              S    S                              SSS     S",
"S              S    S                              S       S",
"S                   S                              S       S",
"S                   S                              S       S",
"SLLLSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS     SSS",
"SSSSSSSSSSSSSSSS               S                S  S       S",
"S              S               S                S  S       S",
"S              S               S                S  S       S",
"S              SSSSSSSSSSSSSSSSS    SSSSSSSS    SSSSSSS    S",
"S                                   S      S               S",
"S    I  G   K                       S      S               S",
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",
]



level_choice: list[str] = [
"                                                                                   SWLBA",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"                                     B                     ",    
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS   SSSS",
"",
"",
"",
"                                                           ",
"",
"                                                           ",
"                                                           ",
"                                                           ",
"                                                           ",
"                                                           ",
"                                                               ",
"                                                            ",
"                  I  G                 B                        ",
"SSSSCCCSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSLLLSSSSS ",
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",
]


#szélesség:60 karakter
#magasság: 30 sor

#A: barrier
#B: button
#C: Activate
#D: Asztal
#E: enemy
#L: lift
#P: Parketta
#S: street
#s: Szék
#T: Csempe
#W: water
tile_size: int = 32
WIDTH, HEIGHT = 1900, len(level_map_1) * tile_size