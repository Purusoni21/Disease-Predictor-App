import 'dart:convert';
import 'dart:async';
import 'package:http/http.dart' as http;

import 'static.dart';
import 'package:flutter/material.dart';
// ignore: import_of_legacy_library_into_null_safe
import 'package:animated_multi_select/animated_multi_select.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Disease Predictor',
      home: MyHomePage(title: 'Disease Predictor APP'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  static List<String> mainList = StaticData().rawSymptoms;

  List<String> selectedList = [];

  Future<String> predict(List<String> items) async {
    if (items.length == 0) return "Select the appropriate symptoms";
    Map<String, int> jsonMap =
        Map.fromIterable(mainList, key: (e) => e, value: (e) => 0);
    for (var s in items) jsonMap[s] = 1;
    final response = await http.post(
      Uri.parse('http://15.206.194.242:5555/predict'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(jsonMap),
    );
    final responseData = jsonDecode(response.body) as Map<String, dynamic>;
    print(responseData);
    return responseData["result"] ?? "";
  }

  @override
  Widget build(BuildContext context) {
    var width = MediaQuery.of(context).size.width;
    var height = MediaQuery.of(context).size.height;
    return Scaffold(
      // backgroundColor: Colors.deepOrangeAccent.shade100,
      appBar: AppBar(
        title: Text(widget.title),
        backgroundColor: Colors.teal,
        actions: [
          IconButton(
              onPressed: () {
                setState(() {
                  selectedList.clear();
                });
              },
              icon: Icon(Icons.clear_all)),
        ],
      ),
      body: SingleChildScrollView(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            SizedBox(height: 5),
            Text(
              selectedList
                  .map(
                      (e) => e.split("_").map((x) => x.toUpperCase()).join(" "))
                  .join(" , "),
              style: TextStyle(
                color: Colors.teal.shade600,
                fontSize: 15,
              ),
            ),
            Divider(
              height: 30,
              thickness: 4,
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  "Select Symptoms",
                  style: TextStyle(
                    fontSize: 30,
                    fontWeight: FontWeight.bold,
                    color: Colors.teal,
                  ),
                ),
              ],
            ),
            SizedBox(height: 20),
            Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                for (var i = 0; i < mainList.length; i += 4)
                  SingleChildScrollView(
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: <Widget>[
                        Flexible(
                          child: MultiSelectChip(
                            reverseScroll: false,
                            introWidgetWidth: 100,
                            color: Colors.teal.shade300,
                            width: width * 0.245,
                            height: height * 0.12,
                            borderRadius: BorderRadius.circular(15),
                            borderWidth: 3,
                            mainList: mainList.sublist(
                                i,
                                i + 4 > mainList.length
                                    ? mainList.length
                                    : i + 4),
                            onSelectionChanged: (selectedList) {
                              setState(() {
                                selectedList = selectedList;
                              });
                            },
                            widgetList: Map.fromIterable(
                              mainList.sublist(
                                  i,
                                  i + 4 > mainList.length
                                      ? mainList.length
                                      : i + 4),
                              key: (e) => e,
                              value: (e) => Text(
                                e
                                    .split("_")
                                    .map((str) => str.toUpperCase())
                                    .join(" "),
                                style: TextStyle(
                                  color: Colors.black,
                                ),
                              ),
                            ),
                            initialSelectionList: selectedList,
                          ),
                        ),
                      ],
                    ),
                  )
              ],
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton.extended(
        icon: Icon(Icons.online_prediction),
        label: Text("Predict"),
        backgroundColor: Colors.teal,
        shape:
            RoundedRectangleBorder(borderRadius: BorderRadius.circular(16.0)),
        onPressed: () async {
          showModalBottomSheet<void>(
            context: context,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.vertical(
                top: Radius.circular(30),
              ),
            ),
            clipBehavior: Clip.antiAliasWithSaveLayer,
            builder: (BuildContext context) {
              return StatefulBuilder(
                  builder: (BuildContext context, StateSetter setState) {
                return Column(
                  mainAxisAlignment: MainAxisAlignment.start,
                  children: [
                    Row(
                      mainAxisAlignment: MainAxisAlignment.end,
                      children: [
                        TextButton.icon(
                          onPressed: () => Navigator.of(context).pop(),
                          icon: Icon(Icons.close, color: Colors.teal.shade300),
                          label: Text(
                            "Close",
                            style: TextStyle(
                              color: Colors.teal.shade300,
                            ),
                          ),
                        ),
                        SizedBox(width: 20),
                      ],
                    ),
                    SizedBox(height: 50),
                    Text(
                      "Predicted Disease\n\n",
                      style: TextStyle(
                        fontSize: 30,
                        fontWeight: FontWeight.bold,
                        color: Colors.teal,
                      ),
                    ),
                    FutureBuilder<String>(
                        future: predict(selectedList),
                        builder: (context, snapshot) {
                          if (!snapshot.hasData)
                            return CircularProgressIndicator();
                          if (snapshot.data!.isNotEmpty) {
                            return Text(
                              snapshot.data.toString(),
                              style: TextStyle(
                                fontSize: 25,
                                fontWeight: FontWeight.bold,
                                color: Colors.teal,
                              ),
                            );
                          } else {
                            return Text("Error occured while predicting");
                          }
                        }),
                  ],
                );
              });
            },
          );
        },
      ),
    );
  }
}
