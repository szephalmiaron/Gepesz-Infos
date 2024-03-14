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
"S                          F                               S",
"S                                                          S",
"S              SSSSSSSSSSiiiiSS                            S",
"S            SSSSSSSSSSSSSSSSSS                            S",
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
"              I         G                                      ",
"                                       B                        ",
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSLLLSSSSS ",
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",
]




level_map_2: list[str] = [
"SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S              SSSSSSSSSSS                                 S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                                                          S",
"S                          F                               S",
"S                                                          S",
"S              SSSSSSSSSSiiiiSS                            S",
"S            SSSSSSSSSSSSSSSSSS                            S",
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


#szélesség:60 karakter
#magasság: 30 sor

#A: barrier
#B: button
#C: Activate
#D: Asztal
#F: Főbejárat
#E: enemy
#G: Gépész
#I: Infós
#i: Finished_check
#K: Switch
#L: lift
#P: Parketta
#S: street
#s: Szék
#T: Csempe
#W: water
tile_size: int = 32
WIDTH, HEIGHT = 1900, len(level_map_1) * tile_size