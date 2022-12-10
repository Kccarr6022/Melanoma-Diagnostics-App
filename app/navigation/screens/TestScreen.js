import * as React from "react";
import { View, Text, StyleSheet, Pressable } from "react-native";
import Ionicons from "react-native-vector-icons/Ionicons";

export default function TestScreen({ navigation }) {
  return (
    <View
      style={{
        flex: 1,
        alignItems: "center",
        backgroundColor: "#1E1E25",
      }}
    >
      <Text
        onPress={() => alert("This is the 'Test' screen")}
        style={styles.textTitle}
      >
        Picture
      </Text>

      <Pressable style={styles.button}>
        <Text style={styles.text}>Capture</Text>
      </Pressable>
      <Pressable style={styles.button}>
        <Text style={styles.text}>Upload</Text>
      </Pressable>

      <View style={styles.imgCanvas}></View>

      <Pressable style={styles.button}>
        <Text style={styles.text}>Submit</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  textTitle: {
    right: "25%",
    fontSize: 58,
    fontFamily: "AmericanTypewriter-Condensed",
    fontWeight: "bold",
    padding: 10,
    letterSpacing: 1,
    color: "white",
  },
  button: {
    marginBottom: 5,
    marginTop: 5,
    minWidth: "90%",
    flexDirection: "row",
    justifyContent: "center",
    borderRadius: 20,
    elevation: 3,
    backgroundColor: "#AF2F32",
  },
  imgCanvas: {
    marginBottom: 5,
    marginTop: 5,
    minWidth: "70%",
    minHeight: "55%",
    flexDirection: "row",
    justifyContent: "center",
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 10,
    elevation: 3,
    backgroundColor: "white",
  },
  text: {
    fontSize: 34,
    fontFamily: "AmericanTypewriter-Condensed",
    fontWeight: "bold",
    padding: 10,
    letterSpacing: 1,
    color: "black",
  },
});
