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

rivets.formatters.take = function(array, offset, n){
  if (offset + n > array.length){
    // start again from beginning of the array
    var rest = offset + n - array.length;
    return array.slice(offset).concat(array.slice(0, rest));
  } else {
    return array.slice(offset, offset + n);
  }
}

rivets.formatters.eq = function(val, arg){
  return val == arg
}

var players = [
  { name: 'Hans' },
  { name: 'Alexander D.' },
  { name: 'Fabien' },
  { name: 'Simon' },
  { name: 'Jan' }
];

var states = {
  display: 3,
  player1: {
    offset: 0
  },
  player2: {
    offset: 0
  },
  player3: {
    offset: 0
  },
  player4: {
    offset: 0
  }
}

$(function() {
  rivets.bind($('body'), { players: players, states: states });
});

var nextPlayer = function(list){
  var newOffset = states[list].offset + 1
  states[list] = {
    offset: newOffset >= players.length ? 0 : newOffset
  }
}
