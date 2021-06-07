enum FeedbackKind {
  liked,
  disliked
}

export default class FeedbackItem {
  comment: string
  type: FeedbackKind
  weak: number | undefined
  year: number | undefined

  constructor (comment: string, type: FeedbackKind, year: number | undefined, weak: number | undefined) {
    this.comment = comment
    this.type = type
    this.year = year
    this.weak = weak
  }
}

export { FeedbackKind, }
