package com.example.pacman;

import javafx.application.Application;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ButtonType;
import javafx.scene.control.Label;
import javafx.scene.layout.*;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.EventListener;
import java.util.Stack;

public class HelloApplication extends Application {
    private double x = 0;
    private double y = 100;

    @Override
    public void start(Stage stage) throws Exception {
        Circle circle = new Circle(20);
        circle.setCenterX(x);
        circle.setCenterY(y);
        circle.setFill(Color.BLUE);

        Button left = new Button();
        Button right = new Button();
        Button up = new Button();
        Button down = new Button();

        left.setOnAction();


        Pane pane = new Pane();
        pane.getChildren().add(circle);

        Scene scene = new Scene(pane, 400,400);
        stage.setScene(scene);
        stage.show();
    }

    class leftt implements EventHandler<>{
        public void
    }

    public static void main(String[] args) {
        launch();
    }
}

