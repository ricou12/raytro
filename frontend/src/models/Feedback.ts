export default class Feedback {
  liked: Array<string>
  disliked: Array<string>
  year: number|undefined
  weak: number|undefined
  requiredLiked: number
  requiredDisliked: number

  constructor (minimalLikes = 1, minimalDislikes = 1) {
    this.requiredLiked = minimalLikes
    this.requiredDisliked = minimalDislikes
    this.liked = []
    this.disliked = []
  }

  public clean (): void {
    this.liked = this.liked.filter(item => item.length > 5)
    this.disliked = this.disliked.filter(item => item.length > 5)
  }

  public isValid (): boolean {
    return this.liked.length >= this.requiredLiked && this.disliked.length >= this.requiredDisliked
  }
}
