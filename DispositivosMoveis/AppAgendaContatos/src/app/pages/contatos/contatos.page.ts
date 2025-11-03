import { Component } from '@angular/core';
import { AlertController, ToastController } from '@ionic/angular';

interface Contato {
  nome: string;
  email: string;
  telefone?: string;
  nascimento?: string;
  horaContato?: string;
}

@Component({
  selector: 'app-contatos',
  templateUrl: './contatos.page.html',
  styleUrls: ['./contatos.page.scss'],
  standalone: false,
})
export class ContatosPage {
  contatos: Contato[] = [];
  novoContato = {
    nome: '',
    email: '',
    telefone: '',
    nascimento: '',
    horaContato: ''
  };

  constructor(private alertCtrl: AlertController, private toastCtrl: ToastController) {}

  private async presentToast(message: string, color: 'success' | 'danger' | 'warning' = 'success', duration = 2000) {
    const toast = await this.toastCtrl.create({ message, duration, color });
    await toast.present();
  }


  private async presentAlert(message: string, header = 'Aviso') {
    const alert = await this.alertCtrl.create({
      header,
      message,
      buttons: ['OK']
    });
    await alert.present();
  }
  
  
  async salvarContato() {
    if (!this.novoContato.nome || !this.novoContato.email) {
      await this.presentAlert('Preencha pelo menos o nome e o e-mail!', 'Erro');
      return;
    }
    this.contatos.push({ ...this.novoContato });
    this.novoContato = { nome: '', email: '', telefone: '', nascimento: '', horaContato: '' };
    await this.presentToast('Contato salvo com sucesso!', 'success');
  }


  async excluirContato(index: number) {
    const alert = await this.alertCtrl.create({
      header: 'Excluir Contato',
      message: 'Deseja realmente excluir este contato?',
      buttons: [
        { text: 'Cancelar', role: 'cancel' },
        {
          text: 'Excluir',
          handler: () => {
            this.contatos.splice(index, 1);
          }
        }
      ]
    });
    await alert.present();
  }
}