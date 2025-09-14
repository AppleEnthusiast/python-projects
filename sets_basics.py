anna_playlist = {"Penny Lane", "Let It Be", "Hey Jude", "Yesterday"}
jenny_playlist = {"Hey Jude", "Yellow Submarine", "Let It Be", "Something"}

print("anna:",anna_playlist)
print("jenny:",jenny_playlist)

print()
print("union (all songs):",anna_playlist | jenny_playlist)

print()
print("intersection (songs both anna and jenny like):",anna_playlist & jenny_playlist)

print()
print("difference (songs in annas playlist):",anna_playlist-jenny_playlist)

print()
print("difference (songs in jenny's playlist):",jenny_playlist-anna_playlist)

print()
print("symmetric difference (songs only in one playlist):", anna_playlist^jenny_playlist)
