from nba_scrape import NBA

player = league.get_player('Lebron James')
player.get_stats(['PTS'],2018,mode=mode)