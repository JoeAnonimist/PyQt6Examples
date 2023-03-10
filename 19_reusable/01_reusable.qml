import QtQuick

Rectangle {
    
    height: 240
    width: 320
    color: "lightsteelblue"
    
    Text {
        
        anchors.horizontalCenter: parent.horizontalCenter
        text: "Custom QML component.\n\n" + 
              "1. Select the control\n" +
              "Pres Ctrl+C, Ctrl+X or Ctrl-V\n" + 
              "to change the icon."
    
    }
    
    Clipboard {
        anchors.centerIn: parent
    }
}
