import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './header/header.component';
import { DefaultService} from '../../generated'
import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule, HttpHandler } from '@angular/common/http';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HeaderComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent implements OnInit {
  title = 'frontend';
  players: any;

  constructor(private defaultService: DefaultService) {}

  ngOnInit() {
    this.defaultService.readPlayersPlayersGet(0, 100).subscribe(data => {this.players = data; console.log(data)});
  }
}
