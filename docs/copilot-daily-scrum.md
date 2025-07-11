# Copilotをデイリースクラムで活用する方法

- 前日の進捗や課題、今日の作業予定を自動で要約・整理（例：IssueやPRの更新内容から要点抽出）
- チームメンバーの進捗状況やブロッカーを一覧化し、共有用サマリを自動生成
- デイリースクラム用の発言テンプレートや進捗報告フォーマットを自動生成
- 進捗や課題の可視化（例：Kanbanボードやバーンダウンチャートの自動更新・出力）
- 「昨日やったこと」「今日やること」「困っていること」をIssueやコメントから抽出し、まとめて提示
- 定型的な進捗報告や課題抽出を自動化し、ミーティング時間の短縮・効率化を支援
- デイリースクラム後の議事録やアクションアイテムを自動でまとめ、チームに共有
- Copilotの提案は必ず内容を確認し、必要に応じて修正・追記する

---

## 前日の進捗や課題、今日の作業予定を自動で要約・整理する具体的な方法

1. **IssueやPull Requestの更新履歴を取得する**
   - gh CLIで `gh issue list --search "updated:>yesterday"` や `gh pr list --search "updated:>yesterday"` などを使い、前日以降の更新を抽出

2. **Copilot ChatやCLIに要約を依頼する**
   - 取得したIssue/PRのタイトル・本文・コメントをプロンプトに貼り付け、「この内容を要約してください」と依頼
   - 例：「以下のIssue/PR更新内容から、進捗・課題・今日やることを箇条書きでまとめてください」

3. **テンプレート化した進捗報告フォーマットに自動で整理**
   - Copilotに「昨日やったこと」「今日やること」「困っていること」の3点でまとめるよう指示
   - 例：
     - 昨日やったこと: ...
     - 今日やること: ...
     - 困っていること: ...

4. **自動化例（コマンド＋プロンプト例）**

    ```sh
    # 前日以降に更新されたIssue一覧を取得
    gh issue list --search "updated:>yesterday" --json number,title,body,updatedAt

    # 前日以降に更新されたPR一覧を取得
    gh pr list --search "updated:>yesterday" --json number,title,body,updatedAt
    ```

- 取得した内容をCopilot Chatに貼り付けて「進捗・課題・今日の予定を要約してください」と依頼
- 必要に応じて、チーム用の進捗サマリや議事録テンプレートに自動で整形

---

## チームメンバーの進捗状況やブロッカーを一覧化し、共有用サマリを自動生成する具体的な方法

1. **各メンバーの担当Issue/PRを抽出する**
   - gh CLIで `gh issue list --assignee <ユーザー名>` や `gh pr list --assignee <ユーザー名>` を使い、担当タスクを取得
   - チーム全員分をfor文やスクリプトでまとめて取得も可能

2. **Issue/PRの進捗状況（open/closed, 状態, コメント数など）を取得**
   - `--json` オプションで `state`, `comments`, `updatedAt` なども取得し、進捗の可視化に活用

3. **Copilot ChatやCLIに「進捗サマリを作成して」と依頼**
   - 取得したデータをCopilotに貼り付け、「各メンバーごとに進捗状況とブロッカーを一覧化してください」と依頼
   - 例：「下記のIssue/PR一覧から、担当者ごとに進捗サマリとブロッカー（未解決・コメント多いもの等）をまとめてください」

4. **サマリのテンプレート例**

```md
| メンバー | 担当Issue/PR | 進捗 | ブロッカー |
|----------|--------------|------|------------|
| user1    | #12, #15     | 進行中 | #15: レビュー待ち |
| user2    | #18          | 完了   | なし         |
```

5. **自動化例（コマンド＋プロンプト例）**

    ```sh
    # user1の担当Issue一覧
    gh issue list --assignee user1 --json number,title,state,comments,updatedAt
    # user2の担当PR一覧
    gh pr list --assignee user2 --json number,title,state,comments,updatedAt
    ```

- 取得した内容をCopilot Chatに貼り付けて「進捗サマリとブロッカーを一覧化してください」と依頼
- 必要に応じて、Markdown表や議事録テンプレートに自動で整形

---

## 進捗や課題の可視化（Kanbanボードやバーンダウンチャートの自動更新・出力）の具体的な方法

1. **Kanbanボードの進捗可視化**
   - GitHub Projects（Kanban型）を利用し、タスクの状態（ToDo/Doing/Done等）をボードで管理
   - gh CLIで `gh project view <project-number> --owner <owner>` でボードの状態を確認
   - `gh project item-list <project-number> --owner <owner> --format json` で各カラムのIssue一覧を取得し、進捗を集計
   - Copilotに「このボードの進捗を要約してください」と依頼し、可視化用サマリを自動生成

2. **バーンダウンチャートの自動生成**
   - タスクの見積もり（ストーリーポイントやEstimate）をIssueやProjectのカスタムフィールドで管理
   - gh CLIやAPIで各タスクの進捗・残ポイントを集計し、日次でデータを取得
   - 取得したデータをExcelやGoogleスプレッドシート、Mermaid記法などでバーンダウンチャート化
   - Copilotに「このデータでバーンダウンチャート用のMermaidコードを生成してください」と依頼

3. **自動化例（コマンド＋プロンプト例）**

    ```sh
    # プロジェクトボードのアイテム一覧を取得
    gh project item-list <project-number> --owner <owner> --format json

    # 各タスクのEstimateや状態を抽出し、日次で集計
    # 例: jqやExcelでポイント合計・残数を算出
    ```

- 取得した進捗データをCopilot Chatに貼り付けて「バーンダウンチャートを作成してください」と依頼
- Mermaid記法やスプレッドシートでグラフ化し、チームで共有

---
