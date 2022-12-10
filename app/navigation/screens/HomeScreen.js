import * as React from "react";
import { View, Text, Image, StyleSheet, Pressable } from "react-native";
import Ionicons from "react-native-vector-icons/Ionicons";

export default function HomeScreen({ navigation }) {
  return (
    <View
      style={{
        flex: 1,
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "#AF2F32",
      }}
    >
      <Text style={styles.talkBubble}>
        Welcome!{"\n"}How may I{"\n"}help you?
      </Text>
      <Image
        source={require("../../assets/talkBubble.png")}
        style={styles.talkBubble_img}
      />
      <Image source={require("../../assets/doctor.png")} />

      <Pressable
        style={styles.button}
        onPress={() => {
          navigation.navigate("Test");
        }}
      >
        <Text style={styles.text}>New Test</Text>
        <Ionicons name="flask" size={32} style={styles.icon}></Ionicons>
      </Pressable>
      <Pressable
        style={styles.button}
        onPress={() => {
          navigation.navigate("History");
        }}
      >
        <Text style={styles.text}>View History</Text>
        <Ionicons name="bar-chart" size={32} style={styles.icon}></Ionicons>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  talkBubble: {
    fontSize: 20,
    fontWeight: "bold",
    maxWidth: "25%",
    position: "absolute",
    bottom: "86.5%",
    right: "12%",
  },
  talkBubble_img: {
    resizeMode: "contain",
    position: "absolute",
    bottom: "55%",
    right: "5%",
    width: 160,
  },
  button: {
    marginBottom: 10,
    marginTop: 10,
    flexDirection: "row",
    justifyContent: "left",
    padding: 10,
    minWidth: "80%",
    borderRadius: 4,
    backgroundColor: "black",
  },
  icon: {
    position: "relative",
    color: "white",
    padding: 2,
  },
  text: {
    position: "relative",
    top: 5,
    fontSize: 26,
    fontFamily: "AmericanTypewriter-Condensed",
    minWidth: 130,
    lineHeight: 21,
    fontWeight: "bold",
    letterSpacing: 1,
    padding: 7,
    color: "white",
  },
});
