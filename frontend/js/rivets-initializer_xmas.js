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

rivets.formatters.eq = function(val, arg){
  return val == arg
}

var rstate = {
  states: {
    kickerStatus: 'booting',
    score_black: 0,
    score_yellow: 0
  }
}

$(function() {
  rivets.bind($('body'), rstate);
});
