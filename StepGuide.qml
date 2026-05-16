import QtQuick 2.15
import QtQuick.Controls 2.15

Column {
    spacing: 10
    property int step: 0

    Timer {
        interval: 2000
        running: true
        repeat: true

        onTriggered: {
            if (step < 3) {
                step++
            } else {
                stop()
            }
        }
    }

    Text {
        text: "Step 1: Alice chooses random bits and bases"
        visible: step >= 0
        color: "white"
    }

    Text {
        text: "Step 2: Bob measures with his bases"
        visible: step >= 1
        color: "white"
    }

    Text {
        text: "Step 3: Mismatched bases are discarded"
        visible: step >= 2
        color: "white"
    }

    Text {
        text: "Step 4: Final key is extracted"
        visible: step >= 3
        color: "white"
    }
}
