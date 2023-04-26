def solution(stats):
    teams = []
    for stat in stats:
        inserted = False
        for team in teams:
            if stat > team[-1]:
                team.append(stat)
                inserted = True
                break
        if not inserted:
            teams.append([stat])
    return len(teams)
