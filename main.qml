import QtQuick 2.15
import QtQuick.Controls 2.15
import "components"

ApplicationWindow {
    visible: true
    width: 1100
    height: 850
    title: "Quantum Key Distribution Simulation"
    color: "#121212"

    property double errorRate: 0.0
    property var finalKey: []

    ScrollView {
        anchors.fill: parent

        Column {
            width: parent.width
            spacing: 20
            padding: 20

            // Protocol selector + run buttons
            Row {
                spacing: 20
                ComboBox {
                    id: protocolSelector
                    model: ["BB84", "B92", "E91"]
                }
                Button {
                    text: "Run Protocol"
                    onClicked: backend.runProtocol(protocolSelector.currentText, false)
                }
                Button {
                    text: "Run with Eve"
                    onClicked: backend.runProtocol(protocolSelector.currentText, true)
                }
            }

            // Alice vs Bob comparison
            Row {
                spacing: 40
                GridView {
                    width: 400; height: 300
                    model: aliceModel
                    cellWidth: 200; cellHeight: 30
                    delegate: Rectangle {
                        width: 200; height: 30
                        color: (base === bobModel.get(index).base) ? "#00ff00" : "#ff4444"
                        Text { anchors.centerIn: parent; text: "Alice Bit: " + bit + " | Base: " + base; color: "white" }
                    }
                }
                GridView {
                    width: 400; height: 300
                    model: bobModel
                    cellWidth: 200; cellHeight: 30
                    delegate: Rectangle {
                        width: 200; height: 30
                        color: (base === aliceModel.get(index).base) ? "#00ff00" : "#ff4444"
                        Text { anchors.centerIn: parent; text: "Bob Bit: " + bit + " | Base: " + base; color: "white" }
                    }
                }
            }

            // Error rate visualization
            BarChart { id: barChart; matches: 0; mismatches: 0 }

            ProgressBar { id: errorRateBar; width: 600; from: 0; to: 1; value: errorRate }
            Text { id: errorRateText; text: "Error Rate: " + Math.round(errorRate * 100) + "%"; font.pixelSize: 16; color: "orange" }

            // Final key display
            Text { id: finalKeyText; text: "Final Key: "; font.pixelSize: 18; color: "lime" }

            // Cipher demo
            Row {
                spacing: 10
                TextField { id: messageInput; placeholderText: "Enter message to encrypt"; width: 300 }

                Button {
                    text: "Encrypt"
                    background: Rectangle { color: "black"; radius: 4 }
                    contentItem: Text { text: qsTr("Encrypt"); color: "white"; anchors.centerIn: parent }
                    onClicked: {
                        var encrypted = backend.encryptMessage(messageInput.text, finalKey)
                        cipherText.text = "Encrypted: " + encrypted
                    }
                }

                Button {
                    text: "Decrypt"
                    background: Rectangle { color: "black"; radius: 4 }
                    contentItem: Text { text: qsTr("Decrypt"); color: "white"; anchors.centerIn: parent }
                    onClicked: {
                        var decrypted = backend.decryptMessage(cipherText.text.replace("Encrypted: ", ""), finalKey)
                        cipherText.text = "Decrypted: " + decrypted
                    }
                }
            }

            Text { id: cipherText; text: ""; color: "cyan"; font.pixelSize: 16 }

            // Educational guide
            StepGuide { }
        }
    }

    // Models
    ListModel { id: aliceModel }
    ListModel { id: bobModel }

    // Connections
    Connections {
        target: backend
        function onUpdateResults(aliceBits, aliceBases, bobBases, bobResults, finalKeyData) {
            aliceModel.clear()
            bobModel.clear()
            var mismatches = 0, matches = 0
            for (var i = 0; i < aliceBits.length; i++) {
                aliceModel.append({ "bit": aliceBits[i], "base": aliceBases[i] })
                bobModel.append({ "bit": bobResults[i], "base": bobBases[i] })
                if (aliceBases[i] !== bobBases[i]) mismatches++
                else matches++
            }
            errorRate = mismatches / aliceBits.length
            finalKey = finalKeyData
            finalKeyText.text = "Final Key: " + finalKey.join("")
            barChart.matches = matches
            barChart.mismatches = mismatches
        }
    }
}
