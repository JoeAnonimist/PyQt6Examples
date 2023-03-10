import QtQuick

/* Row positions its children in a row ie. horizontally. */

Row {
    
    id: row
    spacing: 2
    
    Rectangle {
    
        color: "red"
        width: 50
        height: 50
        
        MouseArea {
        
           anchors.fill:parent
           
            onClicked: {
                console.log("in click event")
                if (parent.id == row) {
                    parent = col }
                else {
                    parent = row
                }
           }
        
        }
        
    }
    
    Rectangle {
        color: "green"
        width: 20
        height: 50
        
        MouseArea {
        
           anchors.fill:parent
           
           onClicked: {
                console.log("in click event")
                if (parent.id == row) {
                    parent = col }
                else {
                    parent = row
                }
           }
        
        }        
        
    }
    
    Rectangle {
        color: "blue"
        width: 50
        height: 20
        
        MouseArea {
        
           anchors.fill:parent
           
           onClicked: {
                console.log("in click event")
                if (parent.id == row) {
                    parent = col }
                else {
                    parent = row
                }
           }
        
        }  
        
    }
    
    Column {
    
        id: col
    }
    

}
