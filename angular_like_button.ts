import { Component } from '@angular/core';

@Component({
    selector: 'like-button',
    template: `
        
    <button class="like-button" [ngClass]="{'liked':isLiked}" (click)="likeTheButton()">
  Like | <span class="likes-counter">{{ initial_likes }}</span>
</button>
    `,
    styles: [`
        .like-button {
            font-size: 1rem;
            padding: 5px 10px;
            color:  #585858;
        }

        .liked {
            font-weight: bold;
            color: #1565c0;
        }
    `]
})

export class LikeButtonComponent {
    public initial_likes = 100;
    public isLiked = false;
    likeTheButton = () => {
    if(this.isLiked)
    this.initial_likes--;
    else
    this.initial_likes++;

    this.isLiked = !this.isLiked
  }
}
