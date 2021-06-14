
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import javax.swing.*;

public class SimpleGUI {

    private ArrayList <Position> positions = new ArrayList<Position>();
    private DrawPanel drawPanel;
    private final Color bgc = new Color(40, 40, 40);

    public static void main(String[] args) {
        SimpleGUI gui = new SimpleGUI();
        gui.go();
    }

    void go() {
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JButton addObjectButton = new JButton("Добавить объект");
            addObjectButton.addActionListener(new AddObjectListener());
        frame.getContentPane().add(BorderLayout.SOUTH, addObjectButton);

        drawPanel = new DrawPanel();
        frame.getContentPane().add(BorderLayout.CENTER, drawPanel);

        frame.setSize(500, 550);
        frame.setResizable(false);
        frame.setVisible(true);
        frame.setBackground(bgc);

        drawPanel.setSize(300, 350);

        System.out.println("frame: " + frame.getWidth() + "x" + frame.getHeight());
        System.out.println("map: " + drawPanel.getWidth() + "x" + drawPanel.getHeight());
        System.out.println("------");

        boolean stop = false;
        while (!stop){
            drawPanel.repaint();
            try {
                Thread.sleep(2);
            } catch (Exception ex) {
                System.out.println("Error sleep");
            }
        }
    }

    class AddObjectListener implements ActionListener{
        public void actionPerformed(ActionEvent event){
            Position pos = new Position();
            pos.setBorders(0, 0, drawPanel.getHeight(), drawPanel.getWidth());
            pos.setPositions(pos.getRandomPosX(), pos.getRandomPosY());
            while(pos.getX() + 70 > drawPanel.getWidth()){
                pos.setPositions(pos.getX() - 1,pos.getY());
            }
            while (pos.getX() - 70 < 0){
                pos.setPositions(pos.getX() + 1,pos.getY());
            }
            while (pos.getY() + 70 > drawPanel.getHeight()){
                pos.setPositions(pos.getX(),pos.getY() - 1);
            }
            while (pos.getY() - 70 < 0){
                pos.setPositions(pos.getX(),pos.getY() + 1);
            }
            pos.setSize(70, 70);
            pos.setSpeed(2);
            pos.setRandomColor();
            positions.add(pos);
            System.out.println(pos.getBorderBottom());
        }
    }

    class DrawPanel extends JPanel {

        public void paintComponent(Graphics g){
            g.setColor(bgc);
            g.fillRect(0, 0, drawPanel.getWidth(), drawPanel.getHeight());
            for (Position pos : positions) {
//                System.out.println(pos.getX() + "x" + pos.getY());
//                g.setColor(Color.white);
                if (pos.getBorderRight() != drawPanel.getWidth()){
                    pos.setBorderRight(drawPanel.getWidth());
                }
                if (pos.getBorderBottom() != drawPanel.getHeight()){
                    pos.setBorderBottom(drawPanel.getHeight());
                }
                pos.move();
                g.setColor(pos.getColor());
                g.fillOval(pos.getX(), pos.getY(), pos.getWidth(), pos.getHeight());
            }
        }
    }
}
