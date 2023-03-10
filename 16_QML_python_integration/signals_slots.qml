import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {

    visible: true
    
    ColumnLayout {

        Button {
        
            text: "Click for a message"
            
            onClicked: {
                some_context.outputStr("Hello World")
            }
        }
        
        Button {
        
            text: "Click for a random number"
            
            onClicked: {
                myLabel.text = some_context.get_random_number(100)
            }
        
        }

        Label {
            id: myLabel
            text: "Some text"
        }
    }
}
