rivets.configure({
  prefix: 'rv',
  preloadData: true,
  rootInterface: '.',
  templateDelimiters: ['{', '}'],
  iterationAlias : function(modelName) {
    return '%' + modelName + '%';
  },
  handler: function(target, event, binding) {
    this.call(target, event, binding.view.models)
  },
  executeFunctions: false
})

rivets.formatters.visiblePlayers = function(playerList, playerId){
  var selectedPlayer = playerList.find(function(e) { return e.id == playerId });
  var indexOfSelectedPlayer = playerList.indexOf(selectedPlayer);
  if (indexOfSelectedPlayer + selectorWindow >= playerList.length) {
    var remainder = indexOfSelectedPlayer + selectorWindow - playerList.length;
    return playerList.slice(indexOfSelectedPlayer - selectorWindow).concat(playerList.slice(0, remainder + 1));
  } else if (indexOfSelectedPlayer - selectorWindow < 0) {
    return playerList.slice(indexOfSelectedPlayer - selectorWindow).concat(playerList.slice(0, indexOfSelectedPlayer + selectorWindow + 1));
  } else {
    return playerList.slice(indexOfSelectedPlayer - selectorWindow, indexOfSelectedPlayer + selectorWindow + 1);
  }
}

rivets.formatters.eq = function(val, arg){
  return val == arg
}

var players = [
  { id: '2', name: 'Hans' },
  { id: '7', name: 'Alexander D.' },
  { id: 'blubb', name: 'Fabien' },
  { id: 'CAT', name: 'Simon' },
  { id: '1', name: 'Jan' },
  { id: 'idontcare', name: 'Jiayi' }
];

var selectorWindow = 1;
var states = {
  teamBlack: {
    attackPlayer: '7',
    defensePlayer: '1'
  },
  teamYellow: {
    attackPlayer: 'CAT',
    defensePlayer: 'idontcare'
  }
};

$(function() {
  rivets.bind($('body'), { players: players, states: states, selectorWindow: selectorWindow });
});

var nextPlayer = function(team, player){
  var playerId = states[team][player];
  var selectedPlayer = players.find(function(e) { return e.id == playerId });
  var indexOfSelectedPlayer = players.indexOf(selectedPlayer);
  if (indexOfSelectedPlayer + 1 == players.length) {
    states[team][player] = players[0].id;
  } else {
    states[team][player] = players[indexOfSelectedPlayer + 1].id;
  }
}
