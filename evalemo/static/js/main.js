var application = function(){

    var init = function(session) {
        console.log("Connected!");
    };

    var error = function() {
        console.log("Disconnected, or failed to connect :-(");
    };

    $('#help').click( function() {
        RobotUtils.onService(function(ALMemory) {
            ALMemory.raiseEvent('yield', 'help');
        });
    });

    $('#quit').click( function() {
        RobotUtils.onService(function(ALMemory) {
            ALMemory.raiseEvent('yield', 'quit');
        });
    });

    // ALMemory Subscriptions
    RobotUtils.subscribeToALMemoryEvent('MovePepper/Cruising', function(value) {
        console.log(value);
        change_message(value);
    });

    // ALMemory Subscriptions
    RobotUtils.subscribeToALMemoryEvent('MovePepper/Turbo', function(value) {
        console.log(value);
        toggle_turbo(value);
    });

    RobotUtils.connect(init, error);
};
