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
"",
"",
"",
"",
"",
"",
"",
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS     SSS",
"                                                       S",
"                                                      S",
"                                                     S",
"                                                    S",
"                                                   S",
"                                                  S",
"                                                 S             ",
"        I G                                     S              ",
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",
]




#szélesség:60 karakter
#magasság: 30 sor

#S: street
#W: water
#L: lift
#B: button
#E: enemy
#A: barrier
tile_size: int = 32
WIDTH, HEIGHT = 1900, len(level_map_1) * tile_size