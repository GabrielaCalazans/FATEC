package jogoadvinha;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.util.Random;
import java.util.prefs.Preferences;
import javax.swing.*;

public class TelaPrincipal extends javax.swing.JFrame {
    
    private int numeroSecreto;
    private int tentativas;
    
    private JLabel labelContador;
    private JTextField campoPalpite;
    private JButton botaoTentar;
    private JButton botaoDica;
    private JButton botaoReiniciar;
    private JLabel labelRecord;
    private JLabel labelApp;
    private JTextField campoUsername;
    private JLabel labelTimer;

    private JLabel labelPergunta;
    private JLabel bigNumeroLabel;
    private JLabel bigIndicadorLabel;
    private JLabel messageLabel;


    private Timer swingTimer;
    private long startTimeMillis;

    private static final java.util.logging.Logger logger = java.util.logging.Logger.getLogger(TelaPrincipal.class.getName());

    private final Preferences prefs = Preferences.userNodeForPackage(TelaPrincipal.class);
    private static final String KEY_RECORD_USER = "record_user";
    private static final String KEY_RECORD_ATTEMPTS = "record_attempts";
    private static final String KEY_RECORD_TIME = "record_time_ms";

    
    public TelaPrincipal() {
        super("Advinhe o número! By Gacalaza");
        initComponents();
        inicializarComponentesExtras();
        iniciarJogo();
        
        setSize(620, 460);
    }
    
    private void iniciarJogo() {
        numeroSecreto = new Random().nextInt(1000) + 1;
        tentativas = 0;

        startTimeMillis = System.currentTimeMillis();
        if (swingTimer != null && swingTimer.isRunning()) swingTimer.stop();
        swingTimer = new Timer(500, e -> {
            long elapsed = System.currentTimeMillis() - startTimeMillis;
            labelTimer.setText("Tempo: " + formatElapsed(elapsed));
        });
        swingTimer.start();

        labelPergunta.setText("<html>Qual é o número secreto?</html>");
        labelPergunta.setForeground(Color.BLACK);
        if (bigNumeroLabel != null) {
            bigNumeroLabel.setText("?");
        }
        if (bigIndicadorLabel != null) {
            bigIndicadorLabel.setText("");
            bigIndicadorLabel.setForeground(Color.DARK_GRAY);
            bigIndicadorLabel.revalidate();
            bigIndicadorLabel.repaint();
        }
        if (messageLabel != null) {
            messageLabel.setText("");
        }
        labelContador.setText("Tentativas: 0");
        campoPalpite.setText("");
        campoPalpite.setEnabled(true);
        botaoTentar.setEnabled(true);
        botaoDica.setEnabled(true);

        carregarEAtualizarRecordLabel();
    }

    private void processarTentativa(ActionEvent evt) {
        if (!botaoTentar.isEnabled()) return;

        String nome = campoUsername.getText();
        if (nome == null || nome.trim().isEmpty()) {
            messageLabel.setText("<html>🚨 Por favor, informe seu nome antes de jogar.</html>");
            messageLabel.setForeground(Color.RED);
            campoUsername.requestFocusInWindow();
            return;
        }
        nome = nome.trim();
        if (!nome.matches("^[A-Za-zÀ-ÖØ-öø-ÿ ]+$")) {
            messageLabel.setText("<html>🚨 Nome inválido. Use apenas letras e espaços.</html>");
            messageLabel.setForeground(Color.RED);
            campoUsername.requestFocusInWindow();
            return;
        }

        try {
            int palpite = Integer.parseInt(campoPalpite.getText().trim());
            tentativas++;
            labelContador.setText("Tentativas: " + tentativas);
            campoPalpite.setText("");

            if (palpite == numeroSecreto) {
                if (swingTimer != null) swingTimer.stop();
                long elapsed = System.currentTimeMillis() - startTimeMillis;

                bigNumeroLabel.setText(String.valueOf(numeroSecreto));
                bigIndicadorLabel.setText("<html><span style='font-family:Dialog; font-size:80px;'>&#10004;</span></html>");
                bigIndicadorLabel.revalidate(); 
                bigIndicadorLabel.repaint();
                bigIndicadorLabel.setForeground(Color.GREEN);
                messageLabel.setText(String.format(
                        "<html> 🎉  PARABÉNS! Você acertou em %d tentativas!<br>O número era %d.</html>",
                        tentativas, numeroSecreto));
                messageLabel.setForeground(new Color(0, 100, 0));

                campoPalpite.setEnabled(false);
                botaoTentar.setEnabled(false);
                botaoDica.setEnabled(false);

                verificarESalvarRecordSeMelhor(campoUsername.getText().trim(), tentativas, elapsed);

            } else if (palpite < numeroSecreto) {
                bigNumeroLabel.setText("?");
                bigIndicadorLabel.setText("▲");
                bigIndicadorLabel.setForeground(new Color(255, 0, 0));
                messageLabel.setText("<html> O número secreto é MAIOR que " + palpite + "!</html>");
                messageLabel.setForeground(new Color(255, 0, 0));
            } else {
                bigNumeroLabel.setText("?");
                bigIndicadorLabel.setText("▼");
                bigIndicadorLabel.setForeground(new Color(0, 100, 255));
                messageLabel.setText("<html> O número secreto é MENOR que " + palpite + "!</html>");
                messageLabel.setForeground(new Color(0, 100, 255));
            }

        } catch (NumberFormatException e) {
            bigIndicadorLabel.setText("");
            messageLabel.setText("<html> 🚨 Digite apenas um número válido 📢 (1-1000).🚨</html>");
            messageLabel.setForeground(Color.RED);
        }
    }
    
    private void darDica(ActionEvent evt) {
        if (!botaoDica.isEnabled()) return;
        
        tentativas += 3;
        labelContador.setText("Tentativas: " + tentativas);
        
        String parOuImpar = (numeroSecreto % 2 == 0) ? "PAR" : "ÍMPAR";

        messageLabel.setText(String.format(
            "<html>💡 DICA: O número secreto é %s. (Custo: 3 Tentativas)</html>", parOuImpar));
        messageLabel.setForeground(new Color(153, 51, 255));
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 661, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 300, Short.MAX_VALUE)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents
    
    private void inicializarComponentesExtras() {
        labelRecord = new JLabel("", SwingConstants.CENTER);
        labelApp = new JLabel("App: Advinhe o número! By Gacalaza", SwingConstants.CENTER);
        labelRecord.setFont(new Font("Arial", Font.PLAIN, 12));
        labelApp.setFont(new Font("Arial", Font.PLAIN, 12));

        labelTimer = new JLabel("00:00", SwingConstants.LEFT);
        labelTimer.setFont(new Font("Arial", Font.BOLD, 20));
        labelTimer.setPreferredSize(new Dimension(200, 30));

        labelContador = new JLabel("Tentativas: 0", SwingConstants.RIGHT);
        labelContador.setFont(new Font("Arial", Font.BOLD, 20));
        labelContador.setPreferredSize(new Dimension(220, 30));

        labelPergunta = new JLabel("Qual é o número secreto?", SwingConstants.CENTER);
        labelPergunta.setFont(new Font("Arial", Font.BOLD, 18));
        labelPergunta.setBorder(BorderFactory.createEmptyBorder(8, 0, 8, 0));

        bigNumeroLabel = new JLabel("?", SwingConstants.CENTER);
        bigNumeroLabel.setFont(new Font("Arial", Font.BOLD, 80));
        bigNumeroLabel.setForeground(Color.DARK_GRAY);

        bigIndicadorLabel = new JLabel("", SwingConstants.CENTER);
        bigIndicadorLabel.setFont(new Font("Arial", Font.BOLD, 80));
        bigIndicadorLabel.setForeground(Color.DARK_GRAY);

        messageLabel = new JLabel("", SwingConstants.CENTER);
        messageLabel.setFont(new Font("Arial", Font.PLAIN, 16));
        messageLabel.setBorder(BorderFactory.createEmptyBorder(8, 8, 8, 8));

        campoUsername = new JTextField(12);
        campoPalpite = new JTextField(10);
        botaoTentar = new JButton("Tentar");
        botaoDica = new JButton("Dica (+3 Tentativas)");
        botaoReiniciar = new JButton("Reiniciar");

        botaoTentar.addActionListener(this::processarTentativa);
        botaoDica.addActionListener(this::darDica);
        botaoReiniciar.addActionListener(e -> iniciarJogo());

        JPanel topoPanel = new JPanel();
        topoPanel.setLayout(new BoxLayout(topoPanel, BoxLayout.Y_AXIS));
        topoPanel.add(labelRecord);
        topoPanel.add(labelApp);

        JPanel tempoTentativasPanel = new JPanel(new BorderLayout(10, 0));
        tempoTentativasPanel.setBorder(BorderFactory.createEmptyBorder(6, 8, 6, 8));
        tempoTentativasPanel.add(labelTimer, BorderLayout.WEST);
        tempoTentativasPanel.add(labelContador, BorderLayout.EAST);

        JPanel centroPanel = new JPanel();
        centroPanel.setLayout(new BorderLayout());
        centroPanel.add(tempoTentativasPanel, BorderLayout.NORTH);
        centroPanel.add(labelPergunta, BorderLayout.CENTER);

        JPanel colunasPanel = new JPanel(new GridLayout(1, 2));
        colunasPanel.setBorder(BorderFactory.createEmptyBorder(10, 20, 10, 20));
        colunasPanel.add(bigNumeroLabel);
        colunasPanel.add(bigIndicadorLabel);
        centroPanel.add(colunasPanel, BorderLayout.SOUTH);

        JPanel mensagemPanel = new JPanel(new BorderLayout());
        mensagemPanel.add(messageLabel, BorderLayout.CENTER);

        JPanel entradaPanel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(4,4,4,4);
        gbc.fill = GridBagConstraints.HORIZONTAL;

        gbc.gridx = 0; gbc.gridy = 0; gbc.weightx = 0.0;
        entradaPanel.add(new JLabel("Seu Palpite (1 a 1000):"), gbc);

        gbc.gridx = 1; gbc.gridy = 0; gbc.weightx = 1.0;
        entradaPanel.add(campoPalpite, gbc);

        gbc.gridx = 2; gbc.gridy = 0; gbc.weightx = 0.0;
        entradaPanel.add(botaoTentar, gbc);

        JPanel dicaPanel = new JPanel();
        dicaPanel.add(botaoDica);
        dicaPanel.add(botaoReiniciar);

        JPanel userPanel = new JPanel(new BorderLayout(8,0));
        userPanel.setBorder(BorderFactory.createEmptyBorder(6, 8, 6, 8));
        userPanel.add(new JLabel("Seu Nome:"), BorderLayout.WEST);
        userPanel.add(campoUsername, BorderLayout.CENTER);

        JPanel painelPrincipal = new JPanel();
        painelPrincipal.setLayout(new BorderLayout());
        painelPrincipal.add(topoPanel, BorderLayout.NORTH);
        painelPrincipal.add(centroPanel, BorderLayout.CENTER);

        JPanel abaixoPanel = new JPanel();
        abaixoPanel.setLayout(new BoxLayout(abaixoPanel, BoxLayout.Y_AXIS));
        abaixoPanel.add(mensagemPanel);
        abaixoPanel.add(userPanel);
        abaixoPanel.add(entradaPanel);
        abaixoPanel.add(dicaPanel);

        painelPrincipal.add(abaixoPanel, BorderLayout.SOUTH);

        getContentPane().setLayout(new BorderLayout());
        getContentPane().add(painelPrincipal, BorderLayout.CENTER);

        pack();
        setLocationRelativeTo(null);
    }



    private void carregarEAtualizarRecordLabel() {
        String user = prefs.get(KEY_RECORD_USER, "<nenhum>");
        int attempts = prefs.getInt(KEY_RECORD_ATTEMPTS, Integer.MAX_VALUE);
        long timeMs = prefs.getLong(KEY_RECORD_TIME, 0L);
        String timeStr = (attempts == Integer.MAX_VALUE) ? "--:--" : formatElapsed(timeMs);
        String attemptsStr = (attempts == Integer.MAX_VALUE) ? "-" : String.valueOf(attempts);
        labelRecord.setText(String.format("Record: %s - Tentativas: %s tempo: %s", user, attemptsStr, timeStr));
    }

    private void verificarESalvarRecordSeMelhor(String user, int attempts, long timeMs) {
        int recordAttempts = prefs.getInt(KEY_RECORD_ATTEMPTS, Integer.MAX_VALUE);
        long recordTime = prefs.getLong(KEY_RECORD_TIME, Long.MAX_VALUE);

        boolean isNewRecord = false;
        if (attempts < recordAttempts) {
            isNewRecord = true;
        } else if (attempts == recordAttempts && timeMs < recordTime) {
            isNewRecord = true;
        }

        if (isNewRecord) {
            prefs.put(KEY_RECORD_USER, user.isEmpty() ? "anônimo" : user);
            prefs.putInt(KEY_RECORD_ATTEMPTS, attempts);
            prefs.putLong(KEY_RECORD_TIME, timeMs);
            carregarEAtualizarRecordLabel();

            // TODO: enviar dados do novo record para API (assíncrono)
            enviarRecordParaApiAsync(user.isEmpty() ? "anônimo" : user, attempts, timeMs);
        }
    }

    private void enviarRecordParaApiAsync(String user, int attempts, long timeMs) {
        // stub - implemente chamada HTTP/REST futuramente
        // Exemplo de payload:
        // { "Nome": user, "Pontuacao": attempts, "NomeApp": "Advinhe o número! By Gacalaza", "Tempo": timeMs }
    }

    private String formatElapsed(long ms) {
        long totalSec = ms / 1000;
        long min = totalSec / 60;
        long sec = totalSec % 60;
        return String.format("%02d:%02d", min, sec);
    }

    public static void main(String args[]) {
        
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ReflectiveOperationException | javax.swing.UnsupportedLookAndFeelException ex) {
            logger.log(java.util.logging.Level.SEVERE, null, ex);
        }
        java.awt.EventQueue.invokeLater(() -> new TelaPrincipal().setVisible(true));
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    // End of variables declaration//GEN-END:variables
}
