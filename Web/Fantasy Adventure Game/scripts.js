const startEventText = "You open your eyes and find yourself laying on the ground, surrounded by tall trees. The sound of a stream can be faintly heard and appears to be coming from deep within the forest.\nWhat will you do?"



function addEvent(text) {
    // create <p> and text
    const newEvent = document.createElement("p");
    const eventText = document.createTextNode(text);
    
    // add class to <p>
    newEvent.classList.add("event-text");

    // insert text into <p>
    newEvent.appendChild(eventText);

    // reference eventBox, then append newEvent to eventBox
    const eventBox = document.getElementById("eventBox");
    console.log(newEvent)
    eventBox.appendChild(newEvent);
}

function addChoice() {
    // create <p> and text
    const newChoice = document.createElement("button");
    const choiceText = document.createTextNode("Choice text");
    
    // add class to <p>
    newChoice.classList.add("choice");

    // insert text into <p>
    newChoice.appendChild(choiceText);

    // reference eventBox, then append newEvent to eventBox
    const choiceBox = document.getElementById("choiceBox");
    choiceBox.appendChild(newChoice);
}


onload = addEvent(startEventText);
