import java.awt.*;

/**
 * Класс для передвижения объекта
 * */

public class Position {

    private int width;
    private int height;

    private int x;
    private int y;

    private int stepX;
    private int stepY;

    private int borderTop;
    private int borderLeft;
    private int borderBottom;
    private int borderRight;

    private int speed;

    private Color color;

    public Position(){
        this(0, 0, 1, 1);
    }

    public Position(int x, int y) {
        this(x, y, 1, 1);
    }

    public Position(int x, int y, int stepX, int stepY) {
        super();
        this.x = x;
        this.y = y;
        this.stepX = stepX;
        this.stepY = stepY;
    }

    public void move(){
        if (x < borderLeft | x > borderRight - width-1){
            stepX = -stepX;
        }
        if (y < borderTop | y > borderBottom - height-1){
            stepY = -stepY;
        }

        x += stepX;
        y += stepY;

//        try {
//            Thread.sleep(speed);
//        } catch (Exception ex) { }
    }

    /**
     * Сеттеры и геттеры
     * */


    public void setSize(int width, int height){
        this.width = width;
        this.height = height;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getWidth() {
        return width;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public int getHeight() {
        return height;
    }

    public void setPositions(int x, int y){
        this.x = x;
        this.y = y;
    }

    public void setX(int x) {
        this.x = x;
    }
    public int getX(){
        return x;
    }

    public int getRandomPosX(){
        return (int) (Math.random() * (borderRight - width-1));
    }

    public void setY(int y) {
        this.y = y;
    }
    public int getY(){
        return y;
    }
    public int getRandomPosY(){
        return (int) (Math.random() * (borderBottom - height-1));
    }


    public void setSteps(int stepX, int stepY){
        this.stepX = stepX;
        this.stepY = stepY;
    }

    public void setStepX(int stepX) {
        this.stepX = stepX;
    }
    public int getStepY(){
        return stepY;
    }

    public void setStepY(int stepY) {
        this.stepY = stepY;
    }
    public int getStepX(){
        return stepX;
    }


    public void setBorders(int borderTop, int borderLeft, int borderBottom, int borderRight){
        this.borderTop = borderTop;
        this.borderLeft = borderLeft;
        this.borderBottom = borderBottom;
        this.borderRight = borderRight;
    }

    public void setBorderBottom(int borderBottom) {
        this.borderBottom = borderBottom;
    }
    public int getBorderBottom() {
        return borderBottom;
    }

    public void setBorderLeft(int borderLeft) {
        this.borderLeft = borderLeft;
    }
    public int getBorderLeft() {
        return borderLeft;
    }

    public void setBorderRight(int borderRight) {
        this.borderRight = borderRight;
    }
    public int getBorderRight() {
        return borderRight;
    }

    public void setBorderTop(int borderTop) {
        this.borderTop = borderTop;
    }
    public int getBorderTop() {
        return borderTop;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }
    public int getSpeed() {
        return speed;
    }

    public void setColor(Color color) {
        this.color = color;
    }
    public Color getColor() {
        return color;
    }

    public void setRandomColor(){
        int red = (int) (Math.random()*255);
        int green = (int) (Math.random()*255);
        int blue = (int) (Math.random()*255);
        color = new Color(red, green, blue);
    }
}