import QtQuick


Rectangle {

    color: "steelblue"
    width: 200
    height: 200
    
    Text {
    
        id: helloWorld
    
        anchors.fill: parent
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        text: "Hello World!"
    
        MouseArea {
        
           anchors.fill: parent
           
            onClicked: {
            
                // Set font size to a random int
                // between 10 and 20
                
                helloWorld.font.pointSize = 
                    Math.floor(Math.random() * 10) + 10;
                    
                console.log(helloWorld.font.pointSize)
           }
        }
    }
}
