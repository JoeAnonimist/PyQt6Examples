import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {

    visible: true
    
    signal messageButtonClicked(string message)
    signal randomNumButtonClicked(int number)
    
    function updateLabel(n) {
        myLabel.text = n
    }
    
    ColumnLayout {

        Button {
            text: "Click for a message"
            onClicked: messageButtonClicked("Hello World...")
        }
        
        Button {
            text: "Click for a random number"
            onClicked: randomNumButtonClicked(100)
        }

        Label {
            id: myLabel
            text: "Some text"
        }
    }
}
